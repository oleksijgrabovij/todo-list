from todo.views import TaskListView, TagListView, TagCreateView, TaskCreateView
from django.urls import path

app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
]
