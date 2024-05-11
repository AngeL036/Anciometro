from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'core/home.html')
    
@login_required
def IndexView(request):
    return render(request,'paginaPrincipal.html')

def register(request):
    data = {
        'form' : CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'] )
            login(request,user)
            return redirect('home')
    return render(request,'registration/register.html', data)

def salir(request):
    logout(request)
    messages.success(request,F"Tu sesion se ha cerrado correctamente")
    return redirect('home')

