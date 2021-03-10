from django.contrib import admin
from django.urls import path, include
from . import views
from . views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', views.homepage, name='home-page'),
    path('calorie_tracker/', views.calorie_tracker, name='calorie-tracker'),
    path('body_fat_percentage/', views.body_fat_percentage, name='body-fat-percentage'),
    path('body_mass_index/', views.body_mass_index, name='body-mass-index'),
    path('calorie_calculator/', views.calorie_calculator, name='cal-calc'),
    #path('forum/', views.forum, name='forum'),
    path('to_do/', views.to_do, name='to-do'),
    path('to_do/update_task/<str:pk>/', views.UpdateTask, name='update-task'),
    path('to_do/delete_task/<str:pk>/', views.DeleteTask, name='delete-task'),
    path('forum/', PostListView.as_view(), name='forum'),
    path('forum/<int:pk>/', PostDetailView.as_view(), name='forum-detail'),
    path('forum/new/', PostCreateView.as_view(), name='forum-create'),
    path('forum/<int:pk>/update/', PostUpdateView.as_view(), name='forum-update'),
    path('forum/<int:pk>/delete/', PostDeleteView.as_view(), name='forum-delete'),
]
