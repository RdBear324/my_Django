from django.shortcuts import render
from .models import Post, Category
# Create your views here.


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog_details.html', context)


def blog_category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'blog_category.html', context)
