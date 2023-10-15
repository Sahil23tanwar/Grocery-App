from django.contrib import admin
from django.urls import path
from grocery import views

urlpatterns = [
    path('',views.index,name='home'),
    path('Next',views.Next,name='Next'),
    path('loginn',views.login,name ='loginn'),
    path('about',views.about,name='about'),
    path('contact',views.contact_view,name='contact'),
    path('logout',views.logout_view,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('editproducts',views.editproducts,name='editproducts'),
    path('addproducts',views.addproducts,name='addproducts'),
    path('editproducts/<int:product_id>',views.deleteproducts),
    path('editproducts/<int:product_id>',views.updateproducts),
    path('addsales',views.addsales,name="addsales")
]
