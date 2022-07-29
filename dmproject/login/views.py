
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def lgin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        User=auth.authenticate(username=username,password=password)
        if User is not None:
            auth.login(request,User)
            return redirect('/')
        else:
            messages.info(request,"invalid login")
            return redirect('lgin')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=fname, last_name=lname,email=email)
                user.save()
                return redirect('lgin')
                print("user created")
        else:
             messages.info(request, "password is not matched")
             return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect("/")