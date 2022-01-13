from django.shortcuts import render, redirect
from django.template import context
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    context={}
    return render(request,"index.html",context)

def signup(request):
    register_form = SignUpForm()
    if request.method == "POST":
        register_form = SignUpForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account has been created.')
            return redirect('index')
        else:
           messages.error(request, register_form.errors)
    context ={'signupform': SignUpForm()}
    return render(request,"signup.html",context)


def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        account = authenticate(username=username,password=password)
        if account is not None:
            login(request, account)
            return redirect('home')
        else:
            messages.warning(request,"Invalid Username or Password")
    context={}
    return render(request,'login.html',context)