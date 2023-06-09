from django.db import models

# Create your models here.
class Product_category(models.Model):
    PC_id=models.IntegerField(primary_key=True)
    PC_name=models.CharField(max_length=100)
    def __str__(self):
        return self.PC_name
class Product(models.Model):
    PC_name=models.ForeignKey(Product_category, on_delete=models.CASCADE)
    P_id=models.IntegerField()
    P_name=models.CharField(max_length=100)
    P_price=models.IntegerField()
    P_description=models.CharField(max_length=100)
    P_date=models.DateField()
    def __str__(self):
        return self.P_name