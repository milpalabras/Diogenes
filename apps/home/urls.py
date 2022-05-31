from django.urls import path
from home import views



urlpatterns = [

    # pagina de inicio
    path('', views.index, name='home'), 
    path('acerca_de_mi', views.acerca_de_mi, name='acerca_de_mi'),   
    

]
