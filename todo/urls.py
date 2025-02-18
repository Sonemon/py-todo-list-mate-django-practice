from django.urls import path
from todo.views import (
    TaskListView,
    TaskCreateView,
    CompleteTaskView,
    UpdateTaskView,
    DeleteTaskView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/new/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/complete/", CompleteTaskView.as_view(), name="task_complete"),
    path("task/<int:pk>/update/", UpdateTaskView.as_view(), name="task_update"),
    path("task/<int:pk>/delete/", DeleteTaskView.as_view(), name="task_delete"),
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/new/", TagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
]
