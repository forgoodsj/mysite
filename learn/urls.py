# coding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',  views.index, name='home'),
    url(r'^add/(\d+)/(\d+)/$', views.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)/', views.add2, name='add2'),
]
#url()中第一项是域名的匹配，尖括号中是views带来的信息， 第二项是与调用view参数，第三项是name，其他模板通过命名来引用URL
#让主URLconf可以链接到polls.urls模块。在mysite/urls.py中插入一个include()：