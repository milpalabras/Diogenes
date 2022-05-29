from django import views
from django.urls import path
from .views import ChartbarrasFNP, circlegastos, Chartingresosgastos, Chartingresosmensuales, Chartcontingresosmensuales

urlpatterns = [
    path('estadisticaFNP/', ChartbarrasFNP, name='barras_FNP'),
    path('estadisticacirclegastos/', circlegastos, name='circlegastos'),
    path('Chartingresosgastos', Chartingresosgastos, name='Chartingresosgastos' ),
    path('Chartingresosmensuales', Chartingresosmensuales, name='Chartingresosmensuales'),
    path('Chartcontingresosmensuales', Chartcontingresosmensuales, name='Chartcontingresosmensuales')


]