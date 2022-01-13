from django.shortcuts import render, redirect
from django.template import context
from .forms import SignUpForm
from django.contrib import messages
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
        messages.success(request, f'Account created for {username}.')
        return redirect('index')
    context ={'signupform': SignUpForm()}
    return render(request,"signup.html",context)