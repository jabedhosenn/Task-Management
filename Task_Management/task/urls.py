from django.urls import path
from . import views

urlpatterns = [
    path('add_task/', views.addTask, name='add_task'),
    path('update_task/<int:id>/', views.updateTask, name='update_task'),
    path('delete_task/<int:id>/', views.deleteTask, name='delete_task'),
]