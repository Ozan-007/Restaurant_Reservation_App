from django.shortcuts import render, redirect
from django.template import context
from .forms import SignUpForm, TableForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    context={}
    return render(request,"home.html",context)

def reservate(request):
    reservation_form =  TableForm()
    if request.method == "POST":
        reservation_form = TableForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            party_size = reservation_form.cleaned_data.get('party_size')
            messages.success(request, f'Table for {party_size} people has been reserverd for you.')
            return redirect('home')
        else:
           messages.error(request, reservation_form.errors)
    context ={'reservation_form': TableForm()}
    return render(request,"reservation.html",context)



def signup(request):
    register_form = SignUpForm()
    if request.method == "POST":
        register_form = SignUpForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account has been created.')
            return redirect('home')
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



def logoutview(request):
    logout(request)
    return redirect('login')