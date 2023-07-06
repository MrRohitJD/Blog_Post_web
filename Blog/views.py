from django.shortcuts import render
from django.shortcuts import HttpResponse
from.models import Post
from django.urls import resolve
# Create your views here.

def blogHome(request):
    post =Post.objects.all()
    print(post)
    context = {'posts': post}
    return render(request, 'blog/bloghome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug =slug).first()
    context = {'posts':post}
    return render(request, 'blog/blogPost.html', context )


