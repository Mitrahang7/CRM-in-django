from django.db import models



class Client(models.Model):
  full_name= models.CharField(max_length=100)
  email= models.EmailField(max_length=100)
  phone= models.CharField(max_length=100)
  address= models.CharField(max_length=100)
  city= models.CharField(max_length=100)
  state= models.CharField(max_length=100)
  zipcode= models.CharField(max_length=100)
  created_at= models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return (f"{self.full_name} {self.email} at {self.created_at}")
  

class Product(models.Model):
  client = models.ForeignKey(Client, on_delete= models.CASCADE, related_name='products')
  name = models.CharField(max_length=100)
  price= models.DecimalField(max_digits=10, decimal_places=2)
  date= models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.name} for {self.client.full_name}"

