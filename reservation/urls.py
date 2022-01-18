from django.urls import path 
from .views import home, loginpage, logoutview, reservate, signup
urlpatterns = [
    path("", home, name="home"),
    path("signup", signup, name="signup"),
    path("login", loginpage, name="login"),
    path("logout", logoutview, name="logout"),
    path("reservation", reservate, name="reservation"),
]
