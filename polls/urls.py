# coding: utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',  views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
#url()中第一项是域名的匹配，尖括号中是views带来的信息， 第二项是与调用view参数，第三项是name，其他模板通过命名来引用URL
#让主URLconf可以链接到polls.urls模块。在mysite/urls.py中插入一个include()：