from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

class CadastroForm(forms.Form):
    nome = forms.CharField(max_length=64, label="Seu Nome:")
    email = forms.EmailField(label="E-mail:")
    senha = forms.CharField(label="Senha:", widget=forms.PasswordInput(), min_length=6)
    confirmar_senha =forms.CharField(label="Confirmar senha:",widget=forms.PasswordInput(), min_length=6)

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=64,label="Username:")
    senha = forms.CharField(label="Senha:", widget=forms.PasswordInput(),min_length=6)

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
                usuario = User.objects.create_user(nome, email, senha)
                usuario.save()
                return HttpResponseRedirect(reverse("amazon:login"))
            else:
                return render(request, "amazon/cadastro.html",{
                    "mensagem": "As senhas não são iguais"
                })
    return render(request, "amazon/cadastro.html",{
        "form": CadastroForm
    })
            

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data["usuario"]
            senha = form.cleaned_data["senha"]
            user = authenticate(request, username=usuario, password=senha)
            if user is not None:
                login(request,user)
                request.session["usuario"] = usuario.capitalize()
                return HttpResponseRedirect(reverse("amazon:index"))
            else: 
                return render(request,"amazon/login.html",{
                    "mensagem": "Usuário ou senha estão errados"
                })
            
    return render(request, "amazon/login.html", {
        "form": LoginForm()
    })

def logout_view(request):
    logout(request)
    request.session["usuario"] = None
    return HttpResponseRedirect(reverse("amazon:index"))