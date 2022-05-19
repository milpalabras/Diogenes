
from finanzas.forms import Gastosform, Ingresosform, Cuentaform

def inject_form(request):
    return {'formgastos': Gastosform(), 'formingresos':Ingresosform(), 'formcuentas':Cuentaform}