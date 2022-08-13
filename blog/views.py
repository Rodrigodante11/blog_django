from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post


def home(request):

    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


def post_detail(request, post_id):
    context = {
        'post': Post.objects.get(pk=post_id)
    }
    return render(request, 'blog/post_detail.html', context)
