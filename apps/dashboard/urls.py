from django import views
from django.urls import path
from .views import ChartbarrasFNP, circlegastos, Chartingresosgastos

urlpatterns = [
    path('estadisticaFNP/', ChartbarrasFNP, name='barras_FNP'),
    path('estadisticacirclegastos/', circlegastos, name='circlegastos'),
    path('Chartingresosgastos', Chartingresosgastos, name='Chartingresosgastos' )

]