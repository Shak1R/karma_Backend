from django.db import models
from django.utils import timezone
from user.models import User


# TODO: add new models category, post
# TODO: category tables title, description
# TODO: post tables title, content, image, published_date, author[FK], category[FK]
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    published_date = models.DateTimeField(auto_now=True)
    #author = models.ForeignKey('user.AbstractUserUser', models.CASCADE)  # TODO: we change that line after adding user model
    category = models.ForeignKey(Category, models.CASCADE)

    def __str__(self):
        return self.title
