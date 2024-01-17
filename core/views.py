from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Usuario
# Create your views here.

def home(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')   

@login_required #Para que somente usuários autenticados acessem o template perfil, em views adicionar a anotação @login_required
def painel(request):
    return render(request, 'painel.html')      

def autenticacao(request):
    '''
    se o usuário digitou algo no formulário e clicou em enviar, o if 
    será verdadeiro, caso contrário, será uma requisição GET e entrara no else.
    -
    '''
    if request.POST:
       usuario = request.POST['usuario']
       senha = request.POST['senha']
       user = authenticate(request, username=usuario, password=senha)
       if user is not None:
        login(request, user)
        return redirect('painel')
       else:
        return redirect('login') 
    else:
        return render(request, 'registration\login.html') 

def desconectar(request):
    logout(request)
    return render(request, 'index.html')  
