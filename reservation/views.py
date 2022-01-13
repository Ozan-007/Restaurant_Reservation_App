from django.shortcuts import render
from django.template import context
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.
def index(request):
    context ={'form': UserCreationForm()}
    return render(request,"index.html",context)