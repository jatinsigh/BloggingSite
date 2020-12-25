from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from .views import (
        PostListView,
        PostDetailView,
        PostCreateView,
        PostUpdateView,
        PostDeleteView,
        UserPostListView)

urlpatterns = [
    path('tasks/', views.required_task, name='required_task'),
    path('about/', views.about, name='about'),
    path('',PostListView.as_view(),name='task_home'),
    path('act/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('act/new/',PostCreateView.as_view(),name='post_create'),
    path('act/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('act/<int:pk>/update/',PostUpdateView.as_view(),name='post_update'),
    path('act/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete')
]
