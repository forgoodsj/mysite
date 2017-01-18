#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    context = {'context':'whoooops'}
    return render(request, 'learn/home.html',context)
#context 是字典，字典第一项在HTML中为调用参数

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c =int(a) + int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    d = int(a) + int(b)
    return HttpResponse(str(d))

def old_add2_redirect(request,a ,b):
    return HttpResponseRedirect(
        reverse('learn:add2', args=(int(a),int(b)))
    )