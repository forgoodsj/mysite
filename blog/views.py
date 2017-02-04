from django.shortcuts import render, get_object_or_404
from .models import Article, Tag, Author
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):

    return render(request, 'blog/index1.html', {
        'article': "article",
        'author': "author",
        'tag':'tag',
    })
class AuthorView(generic.ListView):

    template_name = 'blog/author.html'
    context_object_name = 'author_list'

    def get_queryset(self):
        return Author.objects.order_by('name')[:5]

class TagView(generic.ListView):

    template_name = 'blog/tag.html'
    context_object_name = 'tag_list'

    def get_queryset(self):
        return Tag.objects.order_by('name')[:5]

class ArticleView(generic.ListView):

    template_name = 'blog/HomePage.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.order_by('title')[:5]


def detail(request, article_id):
    p = get_object_or_404(Article, pk=article_id)
    img_list = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
    return render(request, 'blog/detail.html', {
            'article': p,
            'article_list': Article.objects.order_by('title')[:5],
            'img_list':img_list,
            'img':'1.jpg'

        })





