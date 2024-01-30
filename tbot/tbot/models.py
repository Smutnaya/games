from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    article = models.CharField(max_length=10)
    manufacturer = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    dimensions = models.CharField(max_length=1000)
    # date = models.PositiveIntegerField()
    rating = models.FloatField(null=True)
    reviews = models.PositiveIntegerField()
    image = models.FileField(upload_to='static/img')
    datetime = models.DateTimeField()

    def __str__(self):
        return f'{self.name} ({self.article})'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=12)
    address = models.CharField(max_length=250)
    state = models.PositiveIntegerField(null=True)
    datetime = models.DateTimeField()


class Review(models.Model):
    rating = models.PositiveIntegerField()
    text = models.CharField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # date = models.PositiveIntegerField()
    datetime = models.DateTimeField()
