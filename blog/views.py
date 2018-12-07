from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', {'post_list': post_list})


def detail(request, post_id):
    print(post_id)
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/single.html', {'post': post})
