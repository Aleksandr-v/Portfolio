from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Post

def index(request):
    posts = Post.objects.filter(status='published')
    return render(request, 'blog/post/index.html', {'posts':posts})

def detail(request, year, month, day, post):
    post = get_object_or_404(Post, publish__year=year, publish__month=month,
        status='published', publish__day=day, slug=post )
    return render(request, 'blog/post/detail.html', {'post':post})
