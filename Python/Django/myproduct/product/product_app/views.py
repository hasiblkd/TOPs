from django.shortcuts import render,redirect
from product_app.models import *

# Create your views here.

def product(request):
    return render(request,"index.html")

def register(request):
    data=request.POST
    p_name=data.get("product_name")
    p_price=data.get("price")
    p_qty=data.get("quantity")
    p_cate=data.get("category")
    p_decs=data.get("description")
    id=data.get("id")

    if id:
        pr=Product.objects.get(pk=id)
        pr.p_name=p_name
        pr.p_price=p_price
        pr.p_qty=p_price
        pr.p_category=p_cate
        pr.p_desc=p_decs
        pr.save()
        return render(request,"index.html",{"msg":"Update succfully"})
    else:
        Product.objects.create(p_name=p_name,p_price=p_price,p_qty=p_qty,p_category=p_cate,p_desc=p_decs)
        return render(request,"index.html",{"msg":"Product Add Successfully..."})


def display(request):
    products=Product.objects.all()
    return render(request,"display.html",{"products":products})

def delete_product(request):
    id=request.GET.get("id")
    pr=Product.objects.get(id=id)
    pr.delete()
    return redirect("display")

def update_product(request):
    id=request.GET.get("id")
    pr=Product.objects.get(id=id)
    return render(request,"index.html",{"pr":pr})