from django.urls import path
from .import views

urlpatterns = [
        path('', views.indexHome, name="userBlogPage"),
        path('blogPost/<str:slug>/', views.blogPost, name="blogPostPage"),
        path('contact/', views.contact, name="contactpage")
]