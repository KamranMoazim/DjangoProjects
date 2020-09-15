from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post

# Create your views here.

def home(request):
    return render(request, 'home/home.html')
    #return HttpResponse("HOME home")


def contact(request):
    messages.success(request, 'Welcome to Contact')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<3 or len(email)<5 or len(phone)<9 or len(content)<4 :
            messages.error(request, 'Please, Fill The From Correctly!')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your QUERY has submitted!')   
    return render(request, 'home/contact.html')
    #return HttpResponse("contact home")


def about(request):
    messages.success(request, 'Welcome to Our About Page!')
    return render(request, 'home/about.html')
    #return HttpResponse("about home")


def search(request):
    search = request.GET['search']
    allPosts = Post.objects.filter(title__icontains=search)
    if len(search) > 30:
        allPosts = []
        messages.error(request, "Your Query is too LONG!")

    elif len(search) < 1:
        allPosts = []
        messages.error(request, "Please Enter your Query!")

    elif allPosts:
        allPosts = Post.objects.filter(title__icontains=search)   
        messages.success(request, "Your Query Found!")
    else:
        allPosts = Post.objects.filter(title__icontains=search)   
        messages.error(request, "Sorry! Couldn't find your Query!!!")
 
    context = {'allPosts':allPosts, 'query':search}
    return render(request, 'home/search.html', context)


def handleSignup(request):
    if request.method == 'POST':
        name = request.POST['name']
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        email = request.POST['email']
        phone = request.POST['phone']
        country = request.POST['country']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']

        # confirming things
        if len(name) > 10:
            messages.error(request, "Your Username must contain less than 10 characters!")
            return redirect('home')
        
        if not name.isalnum():
            messages.error(request, "Your Username must not contain special characters!")
            return redirect('home')

        if password != confirmPassword:
            messages.error(request, "Your Passwords do not MATCH !")
            return redirect('home')

        # creating user by given from Django default
        myUser = User.objects.create_user(username=name, email=email, password=password)
        myUser.phone = phone
        myUser.country = country
        myUser.first_name = Fname
        myUser.last_name = Lname
        myUser.save()

        messages.success(request, "Your iCoder Account has been Successfully Created!")
        return redirect('home')
    else:
        return HttpResponse("404 - Not Found!")



def handleLogin(request):
    if request.method == 'POST':
        Loginname = request.POST['Loginname']
        Loginpassword = request.POST['Loginpassword']

        user = authenticate(username=Loginname, password=Loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Congratulations! You have Logged into your iCoder Account.")
            return redirect('home')
        else:
            messages.error(request, "Invalid User or Password")
            return redirect('home')

    else:
        return HttpResponse("404 - Not Found!")


def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out!.")
    return redirect('home')