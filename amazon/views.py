from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=64, label="Seu Nome:")
    email = forms.EmailField(label="E-mail:")
    senha = forms.CharField(label="Senha:", widget=forms.PasswordInput(), min_length=6)
    confirmar_senha =forms.CharField(label="Confirmar senha:",widget=forms.PasswordInput(), min_length=6)

# Create your views here.
def index(request):
    if "usuario" not in request.session:
        request.session["usuario"] = None
    return render(request, "amazon/index.html", {"session": request.session})

def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            senha = form.cleaned_data["senha"]
            confirmar_senha = form.cleaned_data["confirmar_senha"]
            if senha == confirmar_senha:
                nome = form.cleaned_data["nome"]
                email = form.cleaned_data["email"]
                usuario = User(username=nome, email=email, password=senha)
                usuario.save()
                return HttpResponseRedirect(reverse("amazon:index"))
            else:
                return render(request, "amazon/cadastro.html",{
                    "mensagem": "As senhas não são iguais"
                })
    return render(request, "amazon/cadastro.html",{
        "form": CadastroForm
    })
            

"""def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email  = form.cleaned_data["email"]
            request.session["usuario"] = email
            return HttpResponseRedirect(reverse("amazon:index"))
            
    return render(request, "amazon/login.html", {
        "form": LoginForm()
    })
"""