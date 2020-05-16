from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from todolist.models import TaskList, Task

# ---------      Task Form   --------- #
class TaskForm(forms.ModelForm):
    """Post form to handle post creation"""

    class Meta:
        model = Task
        fields = ["title", "content", "created", "due_date", "belongs_to"]


# ---------      Task List Form   --------- #
class TaskListForm(forms.ModelForm):
    """Post form to handle post creation"""

    class Meta:
        model = TaskList
        fields = ["name"]

# ---------      Register Form   --------- #
class RegisterForm(forms.ModelForm):
    """Post form to handle post creation"""

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]


# ---------      Login  Form   --------- #
class LoginForm(forms.ModelForm):
    """Login form for the user."""

    class Meta:
        model = User
        fields = ("username", "password")

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data["username"]
            password = self.cleaned_data["password"]
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login provided.")
        return self.cleaned_data
