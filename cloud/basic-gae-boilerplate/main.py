# -*- coding: utf-8 -*-
# from __future__ import \
#     unicode_literals  # pirmās divas rindiņas vajadzīgas lai Python2 + webapp2 atbalstītu latviešu burtis
import webapp2
import os
import jinja2
from models import Contact
from webapp2_extras import sessions
import hmac

# ja problēmas ar jinja2 bibliotēku python instalācijā
# c:\Users\andis\AppData\Local\Google\Cloud SDK\google-cloud-sdk\platform\bundledpython>python -m pip install jinja2 --target=Lib

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        params['logged_in'] = self.session.get('logged_in')
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))

    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()


config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}


class MainHandler(BaseHandler):
    def get(self):
        list = '<ul>'
        for a in range(1, 10):
            list += '<li>Kaut kas: ' + str(a) + '</li>'
        list += '</ul>'
        params = {
            'name': "Andis",
            'saraksts': list,
            'page_title': 'Sakums',
        }
        return self.render_template('index.html', params)


class AboutHandler(BaseHandler):
    def get(self):
        params = {
            'page_title': 'Par mums'
        }
        return self.render_template('about.html', params)


class DatabaseHandler(BaseHandler):
    def get(self):
        params = {
            'page_title': 'Database'
        }
        from models import Message
        messages = Message.query().order(-Message.created).fetch()
        params["messages"] = messages
        params['session'] = self.session.get('foo')
        return self.render_template('database.html', params)

    def post(self):
        from models import Message
        msg_text = self.request.get("message_text")
        msg_notes = self.request.get("message_notes")
        email = self.request.get("email")
        skaitlis = self.request.get("skaitlis")
        if skaitlis.isdigit():
            skaitlis = int(skaitlis)
            row = Message(message_text=msg_text, message_notes=msg_notes, email=email, skaitlis=skaitlis)
            row.put()
            status = 'Addded successfully!'
        else:
            status = 'Please enter number!'
        messages = Message.query().order(-Message.created).fetch()
        params = {'status': status,
                  'messages': messages,
                  'page_title': 'Databases',
                  }
        return self.render_template('database.html', params)


class FormHandler(BaseHandler):
    def get(self):
        params = {
            'page_title': 'Forma'
        }
        return self.render_template('form.html', params)

    def post(self):
        skaitlis = self.request.get('skaitlis')
        kvadrats = int(skaitlis) ** 2
        if skaitlis.isdigit():
            kvadrats = int(skaitlis) ** 2
        else:
            kvadrats = 0
        params = {
            'page_title': 'Forma',
            'ir_dati': True,
            'dati': self.request.get('ievaddati'),
            'skaitlis': skaitlis,
            'kvadrats': kvadrats,
        }
        return self.render_template('form.html', params)


class ContactsHandler(BaseHandler):
    def get(self, contact_id=None):
        params = {
            'page_title': 'Contacts'
        }


        # parbaudam, vai esam logged in
        if self.session.get('logged_in'):
            allow_database = True
        else:
            allow_database = False

        if contact_id:
            contact = Contact.get_by_id(int(contact_id))
        else:
            contact = None
        contacts = Contact.query().order(-Contact.created).fetch()
        params["contacts"] = contacts
        params["contact"] = contact
        params['allow_database'] = allow_database
        return self.render_template('contacts.html', params)

    def post(self, contact_id=None):
        first_name = self.request.get("first_name")
        last_name = self.request.get("last_name")
        email = self.request.get("email")
        if contact_id:
            msg = Contact.get_by_id(int(contact_id))
            msg.first_name = first_name
            msg.last_name = last_name
            msg.email = email
        else:
            msg = Contact(first_name=first_name, last_name=last_name, email=email)
        msg.put()
        return self.redirect_to("contacts")


class EmailHandler(BaseHandler):
    def get(self):
        from google.appengine.api import mail
        message = mail.EmailMessage(
            sender='andis.cirulis@gmail.com',
            subject="Your account has been approved")

        message.to = "andis.cirulis@whitedigital.eu"
        message.body = """Dear Albert:
        Your example.com account has been approved.  You can now visit
        http://www.example.com/ and sign in using your Google Account to
        """
        message.send()


class ContactDeleteHandler(BaseHandler):
    def get(self, contact_id):
        contact = Contact.get_by_id(int(contact_id))
        params = {"contact": contact}
        return self.render_template("contact_delete.html", params=params)

    def post(self, contact_id):
        contact = Contact.get_by_id(int(contact_id))
        contact.key.delete()
        return self.redirect_to('contacts')

class LoginHandler(BaseHandler):
    def get(self):
        return self.render_template('login.html')
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        hash = hmac.new(str(password)).hexdigest()

        if username == 'andis' and hash == 'f7336ed97ecd419f38d5bca6495bc2c7':
            self.session['logged_in'] = True
            return self.redirect_to('contacts')
        else:
            params = {}
            params['incorrect_login'] = True
            return self.render_template('login.html', params)

class LogoutHandler(BaseHandler):
    def get(self):
        self.session['logged_in'] = False
        return self.redirect('contacts')


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/about', AboutHandler),
    webapp2.Route('/form', FormHandler),
    webapp2.Route('/database', DatabaseHandler),
    webapp2.Route('/contacts', ContactsHandler, name="contacts"),
    webapp2.Route('/contacts/<contact_id:\d+>', ContactsHandler),
    webapp2.Route('/contacts/delete/<contact_id:\d+>', ContactDeleteHandler),
    webapp2.Route('/sendmail', EmailHandler),
    webapp2.Route('/login', LoginHandler),
    webapp2.Route('/logout', LogoutHandler),
], debug=True, config=config)
