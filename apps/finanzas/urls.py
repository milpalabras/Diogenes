from django.urls import path
from finanzas import views

urlpatterns = [    
    
    path('cargar-ingresos', views.Cargaringresos, name='cargar_ingresos'),
    path('cargar-gasto', views.Cargargastos, name="cargar_gastos"),
    path('registros', views.RegistrosList.as_view(), name='registros'),
    path('eliminar_registro/<pk>', views.EliminarRegistro, name= 'eliminar_registro'),
    path('editar_registro/<pk>', views.EditarRegistro, name='editar_registro'),
    path('registro/<pk>', views.RegistroDetalle.as_view(), name='registro_detalle'),
    path('cargar-cuenta', views.cuentas, name='cargar_cuentas')
    
]