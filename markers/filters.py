import django_filters

from .models import *

class orderfilter(django_filters.FilterSet):
    
    class Meta:
        
        model = Instituions
        fields = ['institution','category']

    