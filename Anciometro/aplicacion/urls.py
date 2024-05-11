from django.urls import path
from aplicacion import views
 
app_name = 'aplicacion'

urlpatterns = [
    path('', views.IndexView, name='IndexView'),
    path('ansiedad/',views.Ansiedad, name='ansiedad'),
    path('depresion/',views.DepresionView,name='depresion'),
    path('estadisticas/',views.estadisticas,name='estadisticas'),
    path('seguimiento/',views.seguimiento,name='seguimiento'),
    path('respuestas1/',views.respuestas1,name='respuestas1'),
    path('respuestas2/',views.respuesta2,name='respuestas2'),
]