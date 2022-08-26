from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    image = models.TextField()
    category = models.CharField(max_length=200)


    def __str__(self):
        return self.category



class Order(models.Model):
    category = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)


    # def __str__(self):
    #     return self.user
