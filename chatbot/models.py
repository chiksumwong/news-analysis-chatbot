from django.db import models

# Create your models here.
from mongoengine import Document, StringField
 
class News(Document):
    title = StringField(required=True)
    text = StringField(required=True)