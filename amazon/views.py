from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class LoginForm(forms.Form):
    email = forms.CharField(label="Email")
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput(), max_length=8)

# Create your views here.
def index(request):
    if "usuario" not in request.session:
        request.session["usuario"] = None
    return render(request, "amazon/index.html", {"session": request.session})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email  = form.cleaned_data["email"]
            request.session["usuario"] = email
            return HttpResponseRedirect(reverse("amazon:index"))
            
    return render(request, "amazon/login.html", {
        "form": LoginForm()
    })