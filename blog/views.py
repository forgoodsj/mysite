from django.shortcuts import render, get_object_or_404
from .models import Article, Tag, Author
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
'''
class IndexView(generic.ListView):

    template_name = 'blog/index.html'
    context_object_name = 'high_score_blog_list'

    def get_queryset(self):
        return Article.objects.order_by('-score')[:5]

'''

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

    template_name = 'blog/article.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.order_by('title')[:5]

class DetailView(generic.DetailView):
    model = Article
    template_name = 'blog/detail.html'





