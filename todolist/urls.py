from todolist import views
from django.urls import path

urlpatterns = [
    path('', views.todolist1, name='todolist'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('complete/<task_id>', views.complete_task, name='complete_task'),
    path('incomplete/<task_id>', views.incomplete_task, name='incomplete_task'),
]
