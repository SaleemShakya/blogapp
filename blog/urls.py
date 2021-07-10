from django.urls import path
from blog.views import add_post, delete_post, home,about,contact,dashboard,login_view, logout_view, signup, update_post

urlpatterns = [
     
     path('',home, name="home"),
     path('about/',about, name="about"),
     path('contact/',contact, name="contact"),
     path('dashboard/',dashboard, name="dashboard"),
     path('login/',login_view, name="login"),
     path('signup/',signup, name="signup"),
     path('logout/',logout_view, name="logout"),
     path('add-post/',add_post, name="addpost"),
     path('update-post/<int:id>/',update_post, name="updatepost"),
     path('delete-post/<int:id>/',delete_post, name="deletepost")
]
