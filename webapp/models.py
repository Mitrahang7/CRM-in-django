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
