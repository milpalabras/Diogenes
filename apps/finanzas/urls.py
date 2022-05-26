from django.urls import path
from finanzas import views

urlpatterns = [    
    
    path('cargar-ingresos', views.Cargaringresos, name='cargar_ingresos'),
    path('cargar-gasto', views.Cargargastos, name="cargar_gastos"),
    path('registros', views.RegistrosList.as_view(), name='registros'),
    path('eliminar_registro/<pk>', views.EliminarRegistro, name= 'eliminar_registro'),
    path('editar_registro/<pk>', views.EditarRegistro, name='editar_registro'),
    path('registro/<pk>', views.RegistroDetalle.as_view(), name='registro_detalle'),
    path('cuentas', views.CuentasList.as_view(), name='cuentas'),
    path('cuenta/<pk>', views.CuentaDetalle.as_view(), name='cuenta_detalle'),
    path('cargar-cuenta', views.crearcuenta, name='cargar_cuentas'),
    path('editar_cuenta/<pk>', views.Editarcuenta, name="editar_cuenta"),
    path('eliminar_cuenta/<pk>', views.Eliminarcuenta, name="eliminar_cuenta"),
    path('cargar-subcategoria', views.Crearsubcategoria, name="cargar_subcategoria"),
    path('eliminar_subcategoria/<pk>', views.Editarcuenta, name="eliminar_subcategoria"),
    path('editar_subcategoria/<pk>', views.Editarcuenta, name="editar_subcategoria"),
    
]