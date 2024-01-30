from django.db import models

# Create your models here.

class school(models.Model):
    sname=models.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)
    email=models.EmailField('default=some@gmail.com')
    reenteremail=models.EmailField('default=some@gmail.com')

    def __str__(self):
        return self.sname