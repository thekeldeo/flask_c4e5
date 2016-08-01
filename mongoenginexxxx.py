from mongoengine import *

connect('blog',host='mongodb://admin:admin@ds139425.mlab.com:39425/c4e5')

class Person(Document):
    name = StringField()
    age = StringField()
    gender = StringField()
    avatar = StringField()


listPerson = []
# for i in range(3):
#     name1 = input('Nhap ten')
#     age1 = input('Nhap Tuoi')
#     gender1 = input('Gioi tinh')
#     avatar1 = input('Nhap Link anh')
#     person = Person(name = name1, age = age1, gender = gender1, avatar = avatar1)
#     listPerson.append(person)
#
# for person in listPerson:
#     person.save()

for person in Person.objects():
    print (person.name)


# for post in c4e5.objects(author="Khanh"):
#     post.author = "thekeldeo"
#     post.title= ""
#     post.save()
#     break
#
# for post in c4e5.objects():
#     print(post.title)
