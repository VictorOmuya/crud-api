from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
     #path("", views.book_create),
     #path('list/', views.book_list),
     #path("<int:pk>", views.book),
     
     #Using Class views
     path('list/', views.BookList.as_view()),
     path("", views.BookCreate.as_view()),
     path("<int:pk>", views.BookActions.as_view())
]
