from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=30,default="",null=True,blank=True)
    salary = models.IntegerField()
    city = models.CharField(max_length=30,default="",null=True,blank=True)
    # default="", null=True, blank=True  ------ for null value 
    state = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.email
    