#coding=utf-8
from django.shortcuts import render, get_object_or_404
from .models import Question
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context ={
        'latest_question_list': latest_question_list,
    }#接口返回数据
    return render(request, 'polls/index.html', context)
#render快解方式，第二项为导入的模板，第三项为接口（字典）信息
# 为了能够调用这个视图，我们需要将这个视图映射到URL上 —— 利用一个URLconf。
#为了在投票应用目录内部创建URLconf，需要创建一个urls.py文件。
def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    #取数据或报404错误，第一参数为模型，第二参数为关键词参数。相同的还有get_list_or_404()
    return render(request, 'polls/detail.html', {'question': question})

def results(request,question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)