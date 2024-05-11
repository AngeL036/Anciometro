from django.contrib import admin
from django.urls import path,include
from aplicacion import views
urlpatterns = [
    path('',include('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('aplicacion/',include('aplicacion.urls')),
    
]
