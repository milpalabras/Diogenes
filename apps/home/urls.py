from django.urls import path
from home import views



urlpatterns = [

    # pagina de inicio
    path('', views.index, name='home'), 
    
    

]
