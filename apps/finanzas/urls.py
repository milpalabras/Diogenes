from django.urls import path
from finanzas import views

urlpatterns = [    
    #------------Registros
    path('cargar_ingresos', views.Cargaringresos, name='cargar_ingresos'),
    path('cargar_gasto', views.Cargargastos, name="cargar_gastos"),
    path('registros', views.RegistrosList.as_view(), name='registros'),
    path('eliminar_registro/<pk>', views.EliminarRegistro, name= 'eliminar_registro'),
    path('editar_registro/<pk>', views.EditarRegistro, name='editar_registro'),
    path('registro/<pk>', views.RegistroDetalle.as_view(), name='registro_detalle'),
    #----------Cuentas
    path('cuentas', views.CuentasList.as_view(), name='cuentas'),
    path('cuenta/<pk>', views.CuentaDetalle.as_view(), name='cuenta_detalle'),
    path('cargar_cuenta', views.crearcuenta.as_view(), name='cargar_cuentas'),
    path('editar_cuenta/<pk>', views.Editarcuenta.as_view(), name="editar_cuenta"),
    path('eliminar_cuenta/<pk>', views.Eliminarcuenta, name="eliminar_cuenta"),
    #----------Categorias
    path('categorias', views.CategoriaList, name='categorias'),    
    path('editar_subcategoria/<pk>', views.Editarsubcategoria.as_view(), name="editar_subcategoria"),
    path('eliminar_subcategoria/<pk>', views.Eliminarcategoria.as_view(), name="eliminar_subcategoria"),
    
]