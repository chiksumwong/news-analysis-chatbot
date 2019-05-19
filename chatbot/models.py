from django.db import models

# Create your models here.
class Record(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    channel = models.TextField()
    text = models.TextField()
    result = models.TextField()
    probability = models.TextField()

    class Meta:
        db_table = "record"