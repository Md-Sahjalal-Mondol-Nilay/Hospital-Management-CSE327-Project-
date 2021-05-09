from django.db import models

# Create your models here.
class detail(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.IntegerField()
    status = models.CharField(max_length=50, default="register")