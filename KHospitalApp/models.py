from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.CharField(max_length=200)
    color = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    manager = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=65)
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=350)
    def __str__(self):
        return self.name