from flask import Flask, render_template
from mongoengine import *

connect('blog',host='mongodb://admin:admin@ds139425.mlab.com:39425/c4e5')
class Person(Document):
    name = StringField()
    age = StringField()
    gender = StringField()
    avatar = StringField()

listPerson = []
for person in Person.objects():
    listPerson.append(person)


app = Flask(__name__,static_url_path='')

listPage = ["trang chu","trang about","trang san pham", "Lien he"]
listDictionary = [{"name":"trang chu","link":"/"},
                  {"name":"trang about","link":"/about"},
                  {"name":"trang san pham","link":"/product"}
                ]
#xu li du lieu tu database ve dang object
class Page:
    def __init__(self,name,link):
        self.name = name
        self.link = link

listObject = []
for item in listDictionary:
    page = Page(item['name'],item['link'])
    listObject.append(page)

@app.route('/')
def index():
    return render_template("home.html", person = "XXX", title = "My first Website", pages = listPage, pageObjects = listObject, listPerson = listPerson)

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run()