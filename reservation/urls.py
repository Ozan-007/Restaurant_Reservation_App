from django.urls import path 
from .views import index, loginpage, signup
urlpatterns = [
    path("", index, name="index"),
    path("signup", signup, name="signup"),
    path("login", loginpage, name="login"),
]
