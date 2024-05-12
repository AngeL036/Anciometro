import random
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def home(request):
    
    phrases = [
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día. - Robert Collier",
        "El único modo de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
        "La disciplina es el puente entre metas y logros. - Jim Rohn",
        "El optimismo es la fe que conduce al logro. Nada puede hacerse sin esperanza y confianza. - Helen Keller",
        "El fracaso es la oportunidad de comenzar de nuevo, pero con más inteligencia. - Henry Ford",
        "El único límite para tus logros está en tus propias creencias. - Brian Tracy",
        "El éxito no es la clave de la felicidad. La felicidad es la clave del éxito. Si amas lo que estás haciendo, serás exitoso. - Albert Schweitzer",
        "El camino hacia el éxito y la grandeza está siempre en construcción. - Zig Ziglar",
        "Lo importante no es cuántas veces te caes, sino cuántas te levantas. - Vince Lombardi",
        "No cuentes los días, haz que los días cuenten. - Muhammad Ali",
        "El éxito es la suma de pequeños esfuerzos repetidos día tras día. - Robert Collier",
        "La única forma de hacer un gran trabajo es amar lo que haces. - Steve Jobs",
        "Cree que puedes y estarás a medio camino. - Theodore Roosevelt",
        "No tienes que ser grande para empezar, pero tienes que empezar para ser grande. - Zig Ziglar",
        "Nunca es tarde para ser lo que podrías haber sido. - George Eliot",
        "El único lugar donde el éxito llega antes que el trabajo es en el diccionario. - Vidal Sassoon",
        "Cada día es una nueva oportunidad para cambiar tu vida. - Unknown",
        "El éxito no es para los débiles de corazón, ni para los que quieren ganar sin sudar. - Unknown",
        "La distancia entre tus sueños y la realidad se llama acción. - Unknown",
        "El secreto del éxito es empezar antes de estar listo. - Marie Forleo"
    ]
    random_phrase = random.choice(phrases)
    
    
    return render(request, 'core/home.html',{'random_phrase': random_phrase})
    
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

