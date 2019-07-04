from django.urls import path
from . import views

app_name = 'blog_posts'
url_patterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_create, name='post_new'),
    path('edit/<int:pk>/', views.post_update, name='post_edit'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),

]
