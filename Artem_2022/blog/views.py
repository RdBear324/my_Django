from django.shortcuts import render
from .models import Post, Category, Comment
from .forms import CommentForm

# Create your views here.


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    comments = post.posts.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            comment_form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    }
    return render(request, 'blog_details.html', context)


def blog_category(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'blog_category.html', context)


# def category_detail(request, pk):
#     category = Category.object.get(pk=pk)
#     context = {
#         'category' : category
#     }
#     return render(request, 'category_details.html', context)

