from bs4 import BeautifulSoup ############PYTHON 3
# from BeautifulSoup import BeautifulSoup
from urllib.request import urlopen ############PYTHON 3
# from urllib2 import urlopen

# open or create CSV file
csv_file = open("email_list.csv", "w")

url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()
soup = BeautifulSoup(response,"html.parser") ############PYTHON 3

print(soup.html.head.title.string)  # should be: Scrapebook | by SmartNinja

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html,"html.parser")
        # get email and save it into CSV file
        #email = person_soup.find("span", attrs={"class": "email"}).string
        #print(email)
        person_data = {}
        #lets find name
        h1 = person_soup.findAll('h1')[1]
        person_data['name'] = h1.get_text()
        print(person_data['name'])
        #lets find everything else
        xx = person_soup.findAll("li")
        for x in xx:
            li_element = x.get_text()
            if (li_element.find('Email') != -1):
                person_data['email'] =  li_element.split(': ')[1]
            if (li_element.find('Gender') != -1):
                person_data['gender'] =  li_element.split(': ')[1]
            if (li_element.find('Age') != -1):
                person_data['age'] =  li_element.split(': ')[1]
            if (li_element.find('City') != -1):
                person_data['city'] =  li_element.split(': ')[1]

        # row = "{},{},{},{}".format(person_data['email'],person_data['gender'], person_data['age'],person_data['city'])
        row = ','.join([val for key, val in person_data.items()])
        csv_file.write(row+"\n")  # \n will create a new line

# close CSV file
csv_file.close()