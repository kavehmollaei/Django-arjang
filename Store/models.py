
# from django.utils import timezone
from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
# Create your models here.


def default_city():
        return 'Karaj'



lst_city = ['ah','sh','an']
def validate_city(value):
    if value in lst_city:
        raise ValidationError((f'not valid value: %(val)s'),params={'val':'not'},code='invalid',)



class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(help_text="add age")
    address = models.CharField(max_length=150,help_text="address")
    tel = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Store(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50,default=default_city,validators=[validate_city,])
    state = models.CharField(max_length=50)
    date = models.DateField(default=date.today())

    

    def __str__(self):
        return self.name




class Topic(models.Model):
    topic_name = models.CharField(max_length=128, unique=True,validators=[MinLengthValidator(4)])
   
    


    def __str__(self):
        return self.topic_name


    def display(self):
        print(self) 

Item_sizes = [
    ('U','Unknown'),
    ('S','Small'),
    ('M','Medium'),
    ('L','Large'),
    ('XL','XLarge'),
    ('XXL','XXLarge'),
    ] 

class Page(models.Model):
    
    topic_name = models.ForeignKey(Topic,on_delete=models.CASCADE)
    brand = models.CharField(max_length=255, unique=True,db_column='brand_mark')
    price = models.IntegerField()
    url = models.URLField(unique=True,null=True,blank=True)
    

    def __str__(self):
        return self.brand


    def display(self):
        print(self)


class DataAccessed(models.Model):
    brand = models.ForeignKey(Page,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


class TopicTable(models.Model):
    text = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

class EntryTable(models.Model):
    topic= models.ForeignKey(TopicTable,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."            










