from django.urls import path
from .import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreatBlog.as_view(), name='create_blog'),
    path('details/<slug:slug>', views.blog_details, name='blog_details'),
    path('liked/<pk>/', views.liked, name='liked_post'),
    path('disliked/<pk>/', views.disliked, name='dislike_post'),
    path('my-blogs', views.MyBlog.as_view(), name='my_blogs'),
    path('edit/<pk>/', views.UpdateBlog.as_view(), name='edit_blog'),
]