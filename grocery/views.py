from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import auth,User
from grocery.models import *
from django.contrib.auth import authenticate
from django.contrib.auth import logout
#password is sahil@123
# Create your views here.
def index(request):
    return render(request,"index.html");

def Next(request):
        return render(request,"Next.html");

def logout_view(request):
    logout(request)
    print('logged out');
    return render(request,'index.html');
    

def dashboard(request):
        return render(request,"dashboard.html");

def productmanagement(request):
        return render(request,"productmanagement.html");

def salesmanagement(request):
        return render(request,"salesmanagement.html");

def addproducts(request):
        if request.method=="POST":
               product_id=request.POST.get('product_id')
               pname=request.POST.get('pname')
               price=request.POST.get('price')
               brand=request.POST.get('brand')
               ptype=request.POST.get('ptype')
               quantity=request.POST.get('quantity')
               p=product(product_id=product_id,pname=pname,price=price,brand=brand,ptype=ptype,quantity=quantity);
               p.save();
        return render(request,"addproducts.html");
        
def login(request):
       if request.method=="POST":
           username=request.POST['username']  
           password=request.POST['password']  
           user = auth.authenticate(username=username, password=password)
           if user is not None:
                auth.login(request, user)
                print('logged in')
                return render(request,"dashboard.html")
       else:
         return render(request,"loginn.html")
       
def editproducts(request):
       prdcts=product.objects.all();
       return render(request,"editproducts.html",{'prdcts':prdcts})

def deleteproducts(request,product_id):
       prd=product.objects.get(pk=product_id);
       prd.delete();
       return render(request,"addproducts.html") 

def updateproducts(request,product_id):
       prd=product.objects.get(pk=product_id);
       return render(request,"addproducts.html",{'prd':prd})

def addsales(request):
        if request.method=="POST":
               customer_id=request.POST.get('customer_id')
               cname=request.POST.get('cname')
               pname=request.POST.get('pname')
               price=request.POST.get('price')
               quantity=request.POST.get('quantity')
               c=customer(customer_id=customer_id,cname=cname,pname=pname,price=price,quantity=quantity);
               c.save();
        prdcts=product.objects.all();
        return render(request,"addsales.html",{'prdcts':prdcts}) 

# def editsales(request):
#        cstmr=customer.objects.all()
#        return render(request,"editsales.html",{'cstmr':cstmr}) 

# def deletesales(request,customer_id):
#        cst=customer.objects.get(pk=customer_id);
#        cst.delete();
#        return render(request,"addsales.html") 

# def updatesales(request,customer_id):
#        cst=customer.objects.get(pk=customer_id);
#        return render(request,"editsales.html",)

def about(request):
        return render(request,"about.html");

def contact_view(request):
        if request.method=="POST":
               name=request.POST.get('name')
               phone=request.POST.get('phone')
               email=request.POST.get('email')
               p=contact(name=name,phone=phone,email=email)
               p.save();
        return render(request,"contact.html");
