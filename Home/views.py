from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Contact
from Blog.models import Post
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def blogg(request):
    return render(request, 'home/blogg.html')

def about(request):
    return render(request, 'home/about.html')

def search (request):
    query =request.GET['query']
    if len(query)<10:
        allPosts =[]

    else:
        allPosts= Post.objects.filter(title__icontains=query )
    params={'allPost': allPosts, 'query':query}
    return render(request, 'home/search.html', params)

def contact(request):
    if request.method=="POST":
        Mname = request.POST['Iname']
        Memail = request.POST['Iemail']
        Mmob = request.POST['Imobile']
        Mcontent = request.POST['Icontent']
        if len(Mname)<2 or len(Memail)<3 or len(Mmob)<9 or len(Mcontent)<4:
            messages.error(request, "please fill the form properly....")
        else:
            contact = Contact(name=Mname, email=Memail, phone=Mmob, contact= Mcontent)
            contact.save()
            messages.success(request, "you are query it's submitted successfullyand we will contact youas soon as possible..")
    return render(request, 'home/contact.html')


