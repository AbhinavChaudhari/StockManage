from django.db import models

# Create your models here.


class Issue(models.Model):
    department = models.CharField(max_length=200)
    name_of_reciver = models.CharField(max_length=500)
    particulars = models.CharField(max_length=500)
    qty = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    u_id = models.CharField(max_length=100)
    issue_by = models.CharField(max_length=200)
    issue_date = models.CharField(max_length=200)
    remark = models.CharField(max_length=200)


class Inword(models.Model):
    
    delivery_date =models.DateField()
    u_id = models.CharField(max_length=100)
    name = models.CharField(max_length=500)
    particulars = models.CharField(max_length=1000)
    qty= models.CharField(max_length=100)
    unit= models.CharField(max_length=100)
    remark =models.CharField(max_length=100)
    total =models.CharField(max_length=100)
    paid =models.CharField(max_length=100)
    remaining =models.CharField(max_length=100)
    price =models.CharField(max_length=100)


   
class Stock(models.Model):
    delivery_date =models.DateField()
    u_id = models.CharField(max_length=100)
    particulars = models.CharField(max_length=1000)
    qty= models.CharField(max_length=100)
    unit= models.CharField(max_length=100)
    remark =models.CharField(max_length=100)
    total =models.CharField(max_length=100)
    price =models.CharField(max_length=100)



class Collages(models.Model):
   
    name = models.CharField(max_length=100)
