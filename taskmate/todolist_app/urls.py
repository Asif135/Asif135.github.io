from todolist_app import views
from django.urls import path

urlpatterns = [
    path('', views.todolist, name ="todolist"),
    path('delete/<Task_id>', views.delete_Task, name ="delete_Task"),
    path('edit/<Task_id>', views.edit_Task, name ="edit_Task"),
    path('Complete/<Task_id>', views.Complete_Task, name ="Complete_Task"),
    path('Pending/<Task_id>', views.Pending_Task, name ="Pending_Task"),
]
