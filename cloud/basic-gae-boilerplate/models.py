from google.appengine.ext import ndb


class Message(ndb.Model):
    message_text = ndb.StringProperty()
    message_notes = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    email = ndb.StringProperty()
    skaitlis = ndb.IntegerProperty()


class Contacts(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
