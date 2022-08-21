from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post


def home(request):
    posts = Post.objects.order_by('-data_publicacao')[:5]
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def post_detail(request, post_id):
    context = {
        'post': Post.objects.get(pk=post_id)
    }
    return render(request, 'blog/post_detail.html', context)


def blog(request):

    return render(request, 'blog/blog.html')
