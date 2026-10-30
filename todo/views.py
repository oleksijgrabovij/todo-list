from django.shortcuts import get_object_or_404, redirect
from django.views import generic, View
from todo.models import Task, Tag
from django.urls import reverse_lazy
from todo.forms import TaskForm, TagForm


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    paginate_by = 5 # Number of tasks per page


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5 # Number of tags per page


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TaskStatusUpdateView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk) # Get task or return 404 error
        task.is_done = not task.is_done # Toggle the boolean status
        task.save() # Save changes to the database
        return redirect("todo:task-list")  # Redirect back to home page

