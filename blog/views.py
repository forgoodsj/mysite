from django.shortcuts import render, get_object_or_404
from .models import Article, Tag, Author
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'high_score_blog_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Article.objects.order_by('score')[:5]