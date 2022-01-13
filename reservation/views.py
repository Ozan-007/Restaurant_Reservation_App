from django.shortcuts import render
from django.template import context
from .forms import SignUpForm
# Create your views here.
def index(request):
    context={}
    return render(request,"index.html",context)

def signup(request):
    context ={'form': SignUpForm()}
    return render(request,"signup.html",context)