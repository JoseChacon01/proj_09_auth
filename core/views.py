from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required #Obriga o suario fazer altenticação para acessar determinada pagina, que tenha a especificação "@login_required"
from django.contrib.auth import authenticate, login, logout 
from .models import Usuario #Importando a class
from django.contrib.auth.models import Permission
from .forms import UsuarioForm

def home(request):
    return render(request, 'index.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')

def autenticar(request):
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
        return redirect('perfil')
       else:
        return redirect('login') 
    else:
        return render(request, 'registration\login.html')    
def desconectar(request):
    logout(request)
    return render(request, 'index.html')     

@login_required
@permission_required('core.permissao_01')
def cursos(request):
    return render(request, 'cursos.html')

def cadastro_manual(request):
    usuario = Usuario.objects.create_user(
        username= 'admin5',
        email= 'admin5@gmail.com',
        cpf= '555',
        nome= 'Administrador',
        password= '123',
        idade= 30,
        is_superuser=False,
    )

    permissao_1= Permission.objects.get(codename='permissao_01')
    permissao_2= Permission.objects.get(codename='permissao_02')

    usuario.user_permissions.add(permissao_1, permissao_2)

    usuario.save()
    return redirect('home')

def registro(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    context = {
        'form': form
    }
    return render(request, 'registro.html', context)    
