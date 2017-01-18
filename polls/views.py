#coding=utf-8
from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    #polls:results 在urls.py中命名过。
    # reverse 接收 url 中的 name 作为第一个参数，我们在代码中就可以通过 reverse() 来获取对应的网址（这个网址可以用来跳转，也可以用来计算相关页面的地址），只要对应的 url 的name不改，就不用改代码中的网址。
'''
我们在这里使用两个通用视图：ListView 和 DetailView。
这两个视图分别抽象“显示一个对象列表”和“显示一个特定类型对象的详细信息页面”这两种概念。

每个通用视图需要知道它将作用于哪个模型。 这由model 属性提供。

DetailView期望从URL中捕获名为"pk"的主键值，
因此我们把polls/urls.py中question_id改成了pk以使通用视图可以找到主键值 。

默认情况下，通用视图DetailView 使用一个叫做<app name>/<model name>_detail.html的模板。
在我们的例子中，它将使用 "polls/question_detail.html"模板。
template_name属性是用来告诉Django使用一个指定的模板名字，而不是自动生成的默认名字。
我们也为results列表视图指定了template_name —— 这确保results视图和detail视图在渲染时具有不同的外观，即使它们在后台都是同一个 DetailView。

类似地，ListView使用一个叫做<app name>/<model name>_list.html的默认模板；
我们使用template_name 来告诉ListView 使用我们自己已经存在的"polls/index.html"模板。

在之前的教程中，提供模板文件时都带有一个包含question 和 latest_question_list 变量的context。
对于DetailView ，question变量会自动提供—— 因为我们使用Django 的模型 (Question)，
Django 能够为context 变量决定一个合适的名字。然而对于ListView， 自动生成的context 变量是question_list。
为了覆盖这个行为，我们提供 context_object_name 属性，表示我们想使用latest_question_list。
作为一种替换方案，你可以改变你的模板来匹配新的context变量 —— 但直接告诉Django使用你想要的变量会省事很多。

'''


























'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context ={
        'latest_question_list': latest_question_list,
    }#鎺ュ彛杩斿洖鏁版嵁
    return render(request, 'polls/index.html', context)
#render蹇В鏂瑰紡锛岀浜岄」涓哄鍏ョ殑妯℃澘锛岀涓夐」涓烘帴鍙ｏ紙瀛楀吀锛変俊鎭�
#涓轰簡鑳藉璋冪敤杩欎釜瑙嗗浘锛屾垜浠渶瑕佸皢杩欎釜瑙嗗浘鏄犲皠鍒癠RL涓� 鈥斺�� 鍒╃敤涓�涓猆RLconf銆�
#涓轰簡鍦ㄦ姇绁ㄥ簲鐢ㄧ洰褰曞唴閮ㄥ垱寤篣RLconf锛岄渶瑕佸垱寤轰竴涓猽rls.py鏂囦欢銆�
def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    #鍙栨暟鎹垨鎶�404閿欒锛岀涓�鍙傛暟涓烘ā鍨嬶紝绗簩鍙傛暟涓哄叧閿瘝鍙傛暟銆傜浉鍚岀殑杩樻湁get_list_or_404()
    return render(request, 'polls/detail.html', {'question': question})

def results(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
    #polls:results 在urls.py中命名过


    request.POST 是一个类似字典的对象，让你可以通过关键字的名字获取提交的数据。
    这个例子中，request.POST['choice'] 以字符串形式返回选择的Choice的ID。
    request.POST 的值永远是字符串。

    如果在POST数据中没有提供choice，request.POST['choice']将引发一个KeyError。
    上面的代码检查KeyError，如果没有给出choice将重新显示Question表单和一个错误信息。

    在增加Choice的得票数之后，代码返回一个 HttpResponseRedirect而不是常用的HttpResponse。
    HttpResponseRedirect只接收一个参数：用户将要被重定向的URL。

    在这个例子中，我们在HttpResponseRedirect的构造函数中使用reverse()函数。
    这个函数避免了我们在视图函数中硬编码URL。
    它需要我们给出我们想要跳转的视图的名字和该视图所对应的URL模式中需要给该视图提供的参数。
    在本例中，使用在教程3中设定的URLconf， reverse() 调用将返回一个这样的字符串：
    '''
