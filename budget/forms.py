from django.forms import ModelForm
from .models import Budget
from django import forms

class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'
        labels = {
            'namaAksi': 'Action',
            'monthYear': 'Bulan / Tahun',
            'status': 'Status',
            'totalBiaya': 'Biaya'
        }
        widgets = {
            'namaAksi' : forms.TextInput(
                attrs={
                    'class' : 'form-control mb-2',
                }
            ),
            'monthYear' : forms.Select(
                attrs={
                    'class' : 'form-control mb-2'
                }
            ),
            'status' : forms.Select(
                attrs={
                    'class' : 'form-control mb-2'
                }
            ),
            'totalBiaya' : forms.TextInput(
                attrs={
                    'class' : 'form-control mb-2'
                }
            ),
        }

'''
class NewOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status']
        widgets = {
            'customer' : forms.Select(
                attrs={
                    'class' : 'form-control mb-2',
                }
            ),
            'product' : forms.Select(
                attrs={
                    'class' : 'form-control mb-2'
                }
            ),
            'status' : forms.Select(
                attrs={
                    'class' : 'form-control mb-2'
                }
            ),
        }
'''