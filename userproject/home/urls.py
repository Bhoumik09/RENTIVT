from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [ 
    path('',views.index, name="home"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('cycles',views.cycles,name="cycle"),
    path('books',views.books,name="book"),
    path('matress',views.matress,name="matress"),
    path('lamps',views.lamps,name="lamps")
    
]
