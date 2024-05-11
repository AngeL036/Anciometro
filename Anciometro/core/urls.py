from django.urls import path
from .views import home,IndexView, register,salir
from aplicacion import views


urlpatterns = [
    path('',home,name='home'),
    path('IndexView/',IndexView,name='IndexView'),
    path('register/',register,name='register'),
    path('salir/',salir,name='salir'),

]
