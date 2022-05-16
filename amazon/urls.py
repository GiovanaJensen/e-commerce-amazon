from django.urls import path
from . import views

app_name = "amazon"

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro", views.cadastro, name="cadastro")
    #path("login", views.login, name="login")
]