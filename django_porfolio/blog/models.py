from django.db import models
import datetime


class Post(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(datetime.date.today())
