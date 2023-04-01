from django.urls import path
from home import views
urlpatterns = [
    path("",views.loginpage,name='login'),
    path("login",views.loginpage,name='login'),
    path("register",views.registeruser,name='register'),
    path("logout",views.logoutuser,name='logout'),
    path("home",views.home,name="home")

]