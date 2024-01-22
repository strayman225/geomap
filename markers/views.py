from django.shortcuts import render
from markers.models import *
from .filters import orderfilter



# Create your views here.
def index(request):
    stations = list(Instituions.objects.filter().values())
    
    if 'RO' in request.POST:
        stations = list(Instituions.objects.filter(category="RO").values())
    elif 'TTI' in request.POST:
        stations = list(Instituions.objects.filter(category="TTI").values())
    
    elif 'PO' in request.POST:
        stations = list(Instituions.objects.filter(category="PO").values())
    
    elif 'TAS' in request.POST:
        stations = list(Instituions.objects.filter(category="TAS").values())
    
    elif 'TVI' in request.POST:
        stations = list(Instituions.objects.filter(category="TVI").values())

    elif 'ALL' in request.POST:
        stations = list(Instituions.objects.filter().values())
    
    
    
    
    context ={'stations': stations,
    
               }

    return render(request, 'index.html',context)