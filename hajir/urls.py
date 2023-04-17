from django.urls import include, path, re_path
from . import views
urlpatterns = [
    path("ip-addr", views.get_ip_address, name="")
]