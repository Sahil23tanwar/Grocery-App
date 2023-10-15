from django.contrib import admin
from grocery.models import *

# Register your models here.
admin.site.site_header = "GreenGrocers admin login"
admin.site.site_title = "GreenGrocers Admin Portal"
admin.site.index_title = "Welcome to GreenGrocers Researcher Portal"  
admin.site.register(product)
admin.site.register(customer)
admin.site.register(contact)


