import django_filters

from .models import *

class BudgetFilter(django_filters.FilterSet):
    class Meta:
        model = Budget
        fields = ['status']