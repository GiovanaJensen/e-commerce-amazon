from django.urls import path
from . import views

app_name = "amazon"

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro", views.cadastro, name="cadastro"),
    path("login", views.login_view, name="login"),
    path("logout",views.logout_view, name="logout")
]