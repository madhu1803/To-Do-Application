from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
    FormView,
)

from todolist.forms import RegisterForm, LoginForm, TaskListForm, TaskForm
from todolist.models import TaskList, Task


class TaskListView(LoginRequiredMixin, ListView):
    """List view for the Task List model."""

    template_name = "task/task_list.html"

    def get_queryset(self):
        return TaskList.objects.filter(created_by=self.request.user)


class TaskListDetailView(LoginRequiredMixin, DetailView):
    """Detail view for the Tasks model under Task List."""

    queryset = TaskList.objects.all()
    template_name = "task/task_detail.html"

    def get_queryset(self):
        return TaskList.objects.filter(created_by=self.request.user)


class TaskListCreateView(LoginRequiredMixin, CreateView):
    """Create Task List view for the Task List model."""

    form_class = TaskListForm
    template_name = "task/tasklist_form.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskCreateView(LoginRequiredMixin, CreateView):
    """Create Task view for the Task model."""

    form_class = TaskForm
    template_name = "task/task_form.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskListUpdateView(LoginRequiredMixin, UpdateView):
    """Create view for the post model."""

    form_class = TaskListForm
    template_name = "task/tasklist_form.html"
    queryset = TaskList.objects.all()
    success_url = "/"

    def get_queryset(self):
        return TaskList.objects.filter(created_by=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    """Create view for the post model."""

    form_class = TaskForm
    template_name = "task/task_form.html"
    queryset = Task.objects.all()
    success_url = "/"

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)


class TaskListDeleteView(LoginRequiredMixin, DeleteView):
    """Delete view for the post model."""

    model = TaskList
    success_url = "/"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_queryset(self):
        return TaskList.objects.filter(created_by=self.request.user)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    """Delete view for the post model."""

    model = Task
    success_url = "/"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)


class RegistrationView(CreateView):
    """View for user registration."""

    form_class = RegisterForm
    template_name = "account/register.html"
    success_url = "/"

    def form_valid(self, form):
        self.object = form.save()
        self.object.set_password(self.object.password)
        self.object.save()
        login(self.request, self.object)
        return super().form_valid(form)


class LoginView(FormView):
    """View to handle user's login page."""

    form_class = LoginForm
    template_name = "account/login.html"
    success_url = "/"

    def form_valid(self, form):
        data = form.cleaned_data
        user = authenticate(username=data["username"], password=data["password"])
        login(user=user, request=self.request)
        return super(LoginView, self).form_valid(form)


def logout_view(request):
    """Function to handel logout view."""

    logout(request)
    return HttpResponseRedirect("/login")
