from django.db import models

class News(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modify_date = models.DateTimeField(auto_now=True)
    title = models.TextField()
    body = models.TextField()

    class Meta:
        db_table = "news"