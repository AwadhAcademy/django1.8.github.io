from django.db import models

#  Create your models here.
class livesession_Links(models.Model):
    
    Juniour_calss=models.CharField(max_length=50 , default="")
    Calss9_10=models.CharField(max_length=50 , default="")
    Calss11_12=models.CharField(max_length=50 , default="")
 


class feedback(models.Model):
    product_name=models.CharField(max_length=50)
    Product_quality=models.CharField(max_length=1000)
    description=models.CharField(max_length=500)
    rating=models.CharField(max_length=5)