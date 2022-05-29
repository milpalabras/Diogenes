
from finanzas.forms import Gastosform, Ingresosform, Cuentaform, Categoriaform

def inject_form(request):
    return {'formgastos': Gastosform(), 'formingresos':Ingresosform(), 'formcuentas':Cuentaform, 'formcategorias':Categoriaform}