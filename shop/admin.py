from django.contrib import admin
from .models import Product,Contact,User,UserLogin
# Register your models here.
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(UserLogin)

