from django.urls import path
from . import views


app_name = 'task'

urlpatterns = [
    path('', views.list_task, name='task_list'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/<int:task_id>/', views.detail_task, name='detail_task'),
    path('task/update/<int:task_id>/', views.update_task, name='update_task'),
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
