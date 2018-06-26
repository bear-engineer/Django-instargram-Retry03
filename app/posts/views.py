from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    context = {
        'post':posts,
    }

    return render(request, 'posts/post_list.html', context)

    pass

def post_create(request):
    pass

def post_edit(request):
    pass

def recent_post(request):
    pass

