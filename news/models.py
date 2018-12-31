from django.db import models

# Create your models here.
class News(models.Model):
    title = models.TextField()
    body = models.TextField()
    result = models.TextField(null=True)
    feedback = models.TextField(null=True)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "news"