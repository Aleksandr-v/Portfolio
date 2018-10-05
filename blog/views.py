from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Post

def index(request):
    post = get_object_or_404(Post, id=1)
    return render(request, 'blog/post/index.html', {'post':post})
