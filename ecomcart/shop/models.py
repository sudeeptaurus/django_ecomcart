from django.db import models

# Create your Product models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

# Create your Contact models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    email = models.CharField(max_length=75, default="")
    phone = models.CharField(max_length=75, default="")
    desc = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.name
