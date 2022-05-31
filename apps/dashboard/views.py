

from finanzas.models import Registros
from django.db.models import Sum, Count, Q
from django.db.models.functions import TruncMonth, TruncDay
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.
now=datetime.datetime.now()
@login_required
def ChartbarrasFNP (request):
    labels = []
    dataF = []
    dataN = []
    dataP = []

    queryset = Registros.objects.filter(fecha_de_pago__year=now.year).filter(tipo_de_registro="GAST").annotate(
        mes=TruncMonth('fecha_de_pago')).values('mes').annotate(
            totalF = Sum('importe', filter=Q(categoria__tipo_de_categoria='F')),
            totalN = Sum('importe', filter=Q(categoria__tipo_de_categoria='N')),
            totalP = Sum('importe', filter=Q(categoria__tipo_de_categoria='P')),
            )
    for entry in queryset:
        labels.append((entry['mes']).strftime("%b"))
        dataF.append(entry['totalF'])
        dataN.append(entry['totalN'])
        dataP.append(entry['totalP'])

    context = {'labels':labels, 'dataF':dataF, 'dataN':dataN, 'dataP':dataP}

    return JsonResponse ( data = context)

@login_required
def circlegastos (request):
    
    dataF = []
    dataN = []
    dataP = []
    dataT =[]
    porcentajeF =[]
    porcentajeN =[]
    porcentajeP =[]

    dataF.append(Registros.objects.filter(fecha_de_pago__month=now.month).filter(tipo_de_registro="GAST").filter(categoria__tipo_de_categoria='F').count())
    dataN.append(Registros.objects.filter(fecha_de_pago__month=now.month).filter(tipo_de_registro="GAST").filter(categoria__tipo_de_categoria='N').count())
    dataP.append(Registros.objects.filter(fecha_de_pago__month=now.month).filter(tipo_de_registro="GAST").filter(categoria__tipo_de_categoria='P').count())
    dataT.append(Registros.objects.filter(fecha_de_pago__month=now.month).filter(tipo_de_registro="GAST").values('categoria__tipo_de_categoria').count())
    
    porcentajeF.append (int((dataF[0]*100)/dataT[0]))
    porcentajeN.append (int((dataN[0]*100)/dataT[0]))
    porcentajeP.append (int((dataP[0]*100)/dataT[0]))
    
    
    context = {'dataF':dataF, 'dataN':dataN, 'dataP':dataP, 'dataT':dataT, 'porcentajeF':porcentajeF, 'porcentajeN':porcentajeN, 'porcentajeP':porcentajeP}
    return JsonResponse ( data = context)

@login_required    
def Chartingresosgastos (request):
    labels = []
    dataG =[]
    dataI = []

    queryset = Registros.objects.filter(fecha_de_pago__year=now.year).annotate(
        mes=TruncMonth('fecha_de_pago')).values('mes').annotate(
            totalG = Sum('importe', filter=Q(tipo_de_registro='GAST')),
            totalI = Sum('importe', filter=Q(tipo_de_registro='INGR'))
            )
   

    
    for entry in queryset:
        print (entry)
        labels.append((entry['mes']).strftime("%b"))
        dataG.append(entry['totalG'])
        dataI.append(entry['totalI'])
    

    context = {'labels':labels, 'dataG':dataG, 'dataI':dataI}
    return JsonResponse(data=context)    

@login_required
def Chartingresosmensuales (request):
    labels = []    
    dataI = []
    queryset = Registros.objects.filter(fecha_de_pago__month=now.month).annotate(
        dia=TruncDay('fecha_de_pago')).values('dia').annotate(            
            totalI = Sum('importe', filter=Q(tipo_de_registro='INGR'))
            )
    for entry in queryset:
        print (entry)
        labels.append((entry['dia']).strftime("%b"))        
        dataI.append(entry['totalI'])
    context = {'labels':labels, 'dataI':dataI}
    return JsonResponse(data=context)

@login_required
def Chartcontingresosmensuales (request):    
    dataI = []
    contTOTAL =[]
    queryset = Registros.objects.filter(fecha_de_pago__month=now.month).annotate(
        dia=TruncDay('fecha_de_pago')).values('dia').annotate(            
            ContI = Count('importe', filter=Q(tipo_de_registro='INGR'))
            )
    contTOTAL.append(Registros.objects.filter(fecha_de_pago__month=now.month).filter(tipo_de_registro="INGR").filter(categoria__tipo_de_categoria='I').count())
    for entry in queryset:
        print (entry)
              
        dataI.append(entry['ContI'])
    context = {'dataI':dataI, 'contTOTAL':contTOTAL}
    return JsonResponse(data=context)        
    
            
            



   
