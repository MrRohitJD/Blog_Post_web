from django.shortcuts import render ,HttpResponse ,redirect
from .models import Contact
from Blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login , logout

# Create your views here.
def home(request):
    post =Post.objects.all()
    context = {'posts': post}
    return render(request, 'home/home.html', context)


def blogg(request):
    return render(request, 'home/blogg.html')

def about(request):
    return render(request, 'home/about.html')

def search (request):
    query =request.GET['query']
    if len(query)>78:
        allPost =Post.objects.none()
    else:
        allPosttitle= Post.objects.filter(title__icontains=query )
        allPostauthor= Post.objects.filter(author__icontains=query )
        allPostcontent_0= Post.objects.filter(content_0__icontains=query )
        allPost =allPosttitle.union(allPostauthor,allPostcontent_0)
    if allPost.count()==0:
        messages.error(request, "No search results found. Please refine your query.")
    params={'allPost': allPost, 'query':query}
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

def handleSign(request):
    if request.method=='POST':
        Username =request.POST['Username']
        # dp =request.POST['dp']
        fname =request.POST['fname']
        lname =request.POST['lname']
        mobile =request.POST['mobile']
        email =request.POST['email']
        password =request.POST['password']
        password1 =request.POST['password1']

        if len(Username)>10:
            messages.error(request, "Username must be under 10 character")
            return redirect(home)
        if password != password1:
            messages.error(request, "Password does not match")
            return redirect(home)
        if not Username.isalnum():
            messages.error(request, "Username should only contain Alphabet and numric vlaues")
            return redirect(home)
        myuser = User.objects.create_user(Username, email, password)
        myuser.f_name =fname
        myuser.l_name =lname
        myuser.p_word = password1
        # myuser.ProImg = dp
        messages.success(request, "Your account created successfully")
        return redirect(home)
    else:
        return HttpResponse("Error - 404")
    return redirect(home)

def handleLogIn(request):
    if request.method =='POST':
        logUsername =request.POST['logUsername']
        logpassword =request.POST['logpassword']
        
        user =authenticate(username =logUsername, password =logpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successfully")
            return redirect(home)
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect(home)

    return HttpResponse("404- Not found")


def HandleLogOut(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect(home)


def profileView(request):
    profile =User.objects.all()
    param = {'profile':profile}

    return render(request , 'basic.html', param)