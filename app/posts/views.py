from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts':posts,
    }

    return render(request, 'posts/post_list.html', context)

def post_create(request):
    pass

def post_edit(request):
    pass

def recent_post(request):
    pass

