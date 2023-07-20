from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from.models import Post ,BlogComment
from Home.urls import*
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import resolve
# Create your views here.

def blogHome(request):
    post =Post.objects.all()
    print(post)
    context = {'posts': post}
    return render(request, 'blog/bloghome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug =slug).first()
    post=Post.objects.filter(slug=slug).first()
    post.ViewsCount= post.ViewsCount +1
    post.save()
    print(post.ViewsCount)
    comments= BlogComment.objects.filter(post=post)
    context = {'posts':post, 'comments':comments}
    return render(request, 'blog/blogPost.html', context )


def postComment(request):
    if request.method =='POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno =postSno)
        parantSno =request.POST.get('parantSno')

        # if parantSno=="":
        comments = BlogComment(comment =comment, user=user, post=post)
        comments.save()
        messages.success(request , "Comment successfully")

        # else:
        #     parant = BlogComment.objects.get(sno=parantSno)

        #     comments = BlogComment(comment =comment, user=user, post=post ,parent= parant)
        #     comments.save()
        #     messages.success(request , "Reply successfully")
    return redirect(f"/blog/{post.slug}")