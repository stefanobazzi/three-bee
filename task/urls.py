# urls.py
from django.urls import path
from task.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('crea/', TaskCreate.as_view(), name='task_create'),
    path('aggiorna/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('elimina/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
]
