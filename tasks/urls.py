# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # URL for task list
    path('add/', views.add_task, name='add_task'),  # URL for adding a new task
    path('<int:task_id>/', views.detail_task, name='detail_task'),  # URL to view task details
    path('<int:task_id>/delete_task/', views.delete_task, name = 'delete_task'), #URL to delete task
    path('reset/', views.reset, name = 'reset'), #URL to reset

]