from django.urls import path
from . import views

urlpatterns = [
    path('', views.TasksView),
    path('<int:pk>', views.TaskView),
]
