#coding:utf-8
from django.shortcuts import render
from product.models import Product

# Create your views here.
#产品管理
def product_manage(request):
    username = request.session.get('username','')
    product_list = Product.objects.all()
    return render(request,"product_manage.html", {"user": username,"products":product_list})