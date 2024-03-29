from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from webtest.models import Webcase,Webcasestep

# Create your views here.

# web用例管理
@login_required
def webcase_manage(request):
    webcase_list = Webcase.objects.all()
    username = request.session.get('user','')
    return render(request,"webcase_manage.html",{"user":username,"webcases":webcase_list})

# web用例测试步骤
@login_required
def webcasestep_manage(request):
    username = request.session.get('user','')
    webcasestep_list = Webcasestep.objects.all()
    return render(request,"webcasestep_manage.html",{"user": username,"webcasesteps":webcasestep_list})