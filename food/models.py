from django.db import models

class items(models.Model):
    name=models.CharField(max_length=50)
    image = models.CharField(max_length=500, default="")
    category = models.CharField(max_length=50, default="")
    price=models.IntegerField()

    def __str__(self):
        return f"Id: {self.id} Name: {self.name} Price: {self.price}"

class customers(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    item_id = models.IntegerField(default=0)

    def __str__(self):
        return f"Name: {self.name} Item ID: {self.item_id}"