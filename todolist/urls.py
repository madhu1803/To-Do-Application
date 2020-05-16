from django.urls import path

from todolist import views
from todolist.models import TaskList

urlpatterns = [
    # -----------------       AUTHENTICATION VIEWS  URL        -----------------------#
    path("logout/", views.logout_view, name="logout_view"),
    path("login/", views.LoginView.as_view(), name="login_view"),
    path("register/", views.RegistrationView.as_view(), name="register_view"),
    # -----------------------       LIST VIEW  URL            ------------------------#
    path("", views.TaskListView.as_view(), name="task_list"),
    path(
        "tasklist/<int:pk>/", views.TaskListDetailView.as_view(), name="tasklist_detail"
    ),
    # -----------------------     CREATE VIEW  URL            ------------------------#
    path("task/create/", views.TaskCreateView.as_view(), name="task_create"),
    path(
        "tasklist/create/", views.TaskListCreateView.as_view(), name="tasklist_create"
    ),
    # ------------------           UPDATE VIEW  URL            ------------------------#
    path("task/update/<int:pk>/", views.TaskUpdateView.as_view(), name="task_update"),
    path(
        "tasklist/update/<int:pk>/",
        views.TaskListUpdateView.as_view(),
        name="tasklist_update",
    ),
    # -------------------       DELETE VIEW  URL                -------------------------#
    path("task/delete/<int:pk>/", views.TaskDeleteView.as_view(), name="task_delete"),
    path(
        "tasklist/delete/<int:pk>/",
        views.TaskListDeleteView.as_view(model=TaskList),
        name="tasklist_delete",
    ),
]
