from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    image = models.ImageField(upload_to='upload/')

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    price = models.FloatField()
    remains = models.IntegerField()
    characteristic = models.ManyToManyField(Characteristic)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/')

    def __str__(self):
        return self.name
