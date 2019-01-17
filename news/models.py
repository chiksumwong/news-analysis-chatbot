# from django.db import models

# Create your models here.
from mongoengine import *
import datetime 

class News(Document):
    title = StringField(required=True)
    text = StringField(required=True)
    fake_news_prediction = BooleanField()
    fake_news_probability = DecimalField()
    date_modified = DateTimeField(default=datetime.datetime.utcnow)