
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path("login/", views.login_admin, name="login_dashboard",),
    path("", views.dashboard, name="dashboard")

]
