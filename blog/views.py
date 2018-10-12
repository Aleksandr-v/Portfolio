from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Post
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    template_name = 'blog/post/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'blog'
        return context

class PostDetailView(TemplateView):
    template_name = 'blog/post/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, publish__year=kwargs['year'], publish__month=kwargs['month'],
            status='published', publish__day=kwargs['day'], slug=kwargs['post'])
        context['page'] = 'blog'
        return context

# def index(request):
#     posts = Post.objects.filter(status='published')
#     page = 'blog'
#     return render(request, 'blog/post/index.html', {'posts':posts, 'page':page})

# def detail(request, year, month, day, post):
#     post = get_object_or_404(Post, publish__year=year, publish__month=month,
#         status='published', publish__day=day, slug=post )
#     return render(request, 'blog/post/detail.html', {'post':post})
