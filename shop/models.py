from django.db import models

class Product(models.Model):
    
    product_name = models.CharField(max_length=50,default="")
    product_desc = models.CharField(max_length=200,default="")
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images",default="")
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=50,default='')
    contact_email = models.CharField(max_length=50,default='')
    contact_phoneno = models.CharField(max_length=50,default='')
    contact_msg = models.CharField(max_length=50,default='')
    contact_rate = models.IntegerField(default=0)
    def __str__(self):
        return self.contact_id+" "+self.contact_name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50,default='')
    user_phone = models.CharField(max_length=20,default='')
    user_add1 = models.CharField(max_length=100,default='')
    user_add2 = models.CharField(max_length=100,default='')
    user_city = models.CharField(max_length=20,default='')
    user_state = models.CharField(max_length=20,default='')
    user_pincode = models.CharField(max_length=10,default='')
    user_email = models.CharField(max_length=80,default='')
    user_sq1 = models.CharField(max_length=50,default='')
    user_sq1ans = models.CharField(max_length=50,default='')
    user_sq2 = models.CharField(max_length=50,default='')
    user_sq2ans = models.CharField(max_length=50,default='')
    def __str__(self):
        return self.user_name+" "+self.user_email


class UserLogin(models.Model):
    user_email = models.CharField(max_length=80,default='')
    user_pass = models.CharField(max_length=10,default='')
    user_loggedin = models.BooleanField(default=False)
    def __str__(self):
        return self.user_email

