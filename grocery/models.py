from django.db import models

# Create 
# your models here.
class customer(models.Model):
    customer_id=models.CharField(max_length=100)
    cname=models.CharField(max_length=100)
    pname=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100,default=0) 

    def __str__(self):
        return self.cname;

class product(models.Model):
    product_id=models.CharField(max_length=100)
    pname=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    ptype=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)

    def __str__(self):
        return self.pname;

class contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=100)

    def __str__(self):
        return self.name;