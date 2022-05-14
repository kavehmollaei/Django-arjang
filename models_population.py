import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myWebsite.settings")
django.setup()
from django.conf import settings
from Store.models import Page,Topic,DataAccessed,Person,Store
import random
from faker import Faker







fake=Faker()

topics = ['bags','shoes','glasses','pans','shirts','tshirts','socks','coats','Jackets']


"""
def selectTopic():
    chosenTopic = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    chosenTopic.save()
    return chosenTopic

def populateDatabse():
    for i in range(100):

        fake_brand = fake.company()
        fake_price = fake.random_number() 
        fake_url = fake.url()
        fake_date = fake.date_time()

        fake_Page= Page.objects.get_or_create(topic_name=selectTopic(),brand=fake_brand,price=fake_price,url=fake_url)[0]
        fake_date= DataAccessed.objects.get_or_create(brand=fake_Page,date=fake_date)[0]

populateDatabse()
"""


def add_data_db():
    import random
    for item in range(100):
        fake_name = fake.name()
       
        fake_age = random.randint(1,75)
        fake_address = fake.address()
        fake_tel = fake.phone_number()
        fake_email = fake.email()
        fake_city = fake.city()
        fake_date = fake.date()
        fake_state = fake.currency_code()

        fake_Person = Person.objects.get_or_create(name=fake_name, age=fake_age,address=fake_address,tel=fake_tel,email=fake_email)[0]
        fake_Store = Store.objects.get_or_create(owner=fake_Person,name=fake_name,address=fake_address,city=fake_city,state=fake_state,date=fake_date)

user = Store.objects.all()
lst=[]

for item in user:
    lst.append(item.name)


print(lst)    











