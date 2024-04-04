from django.db import models

# Create your models here.
# class Product(models.Model):
#     name = models.TextField(max_length=50, min_length=3, unique=True)
#     price = models.DecimalField(min_value=0.99, max_value=1000)
#     creation_date = models.DateField(auto_now_add=True)
#     category = models.ForeignKey(Category, on_delete=models.PROTECT)

# class Category(models.Model):
#     name = models.TextField(max_length=50, min_length=3, unique=True)

class Shelter(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=200)
    decsription = models.TextField()
    intake_date = models.DateTimeField(auto_now_add=True)
    shelter = models.ForeignKey(Shelter, on_delete=models.PROTECT)
    def __str__(self):
        return self.name