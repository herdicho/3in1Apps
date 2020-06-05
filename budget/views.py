from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import BudgetForm
from .serializers import BudgetSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def dashboard(request):
   monthYear = MonthYear.objects.all()
   actions = Budget.objects.all().order_by('-date_created')[:5]

   paginator = Paginator(monthYear, 5)
   page = request.GET.get('page')
   try:
      monthYearPage = paginator.page(page)
   except PageNotAnInteger:
      monthYearPage = paginator.page(1)
   except EmptyPage:
      monthYearPage = paginator.page(paginator.num_pages)

   form = BudgetForm()
   if request.method == 'POST':
      form = BudgetForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('/budget/')

   
   totalPemasukan = getTotalPemasukan()
   totalPengeluaran = getTotalPengeluaran()
   balance = totalPemasukan - totalPengeluaran
   
   totalPemasukan = '{0:,}'.format(totalPemasukan)
   totalPengeluaran = '{0:,}'.format(totalPengeluaran)
   balance = '{0:,}'.format(balance)

   context = {
      'monthYear' : monthYear,
      'actions' : actions,
      'monthYearPage' : monthYearPage,
      'form':form,
      'totalPemasukan':totalPemasukan,
      'totalPengeluaran':totalPengeluaran,
      'balance':balance,
   }

   return render(request, 'budget/dashboard.html', context)


def getTotalPemasukan():
   daftarPemasukan = Budget.objects.filter(status="Pemasukan")

   totalPemasukan = 0
   for pemasukan in daftarPemasukan.values_list('totalBiaya', flat=True):
      totalPemasukan += pemasukan

   return totalPemasukan

def getTotalPengeluaran():
   daftarPengeluaran = Budget.objects.filter(status="Pengeluaran")

   totalPengeluaran = 0
   for pengeluaran in daftarPengeluaran.values_list('totalBiaya', flat=True):
      totalPengeluaran += pengeluaran

   return totalPengeluaran


def actionUpdateFrontEnd(request, pk):
   budget = Budget.objects.get(id=pk)
   form = BudgetForm(instance=budget)

   monthYear = MonthYear.objects.get(monthYear=budget.monthYear)

   if request.method == 'POST':
      form = BudgetForm(request.POST, instance=budget)
      if form.is_valid():
         form.save()
         return redirect('/budget/detail/' + str(monthYear.id))

   context = {
      'form' : form
   }

   return render(request, 'budget/update_action.html', context)


def actionDeleteFrontEnd(request, pk):
   actionDelete = Budget.objects.get(id=pk)
   actionDelete.delete()
   monthYear = MonthYear.objects.get(monthYear=actionDelete.monthYear)
   
   redirectLink = '/budget/detail/' + str(monthYear.id)
   
   return redirect(redirectLink)


def actionDetailPerMonth(request, pk):
   monthYear = MonthYear.objects.get(id=pk)
   listActions = Budget.objects.filter(monthYear=monthYear)

   context = {
      'monthYear' : monthYear,
      'listActions' : listActions
   }

   return render(request, 'budget/detail_action.html', context)


@api_view(['GET'])
def apiOverview(request):
   api_urls = {
      'List Action':'/action-list',
      'Detail Action':'/action-detail/<str:pk>',
      'Create Action':'/action-create',
      'Update Action':'/action-update/<str:pk>',
      'Delete Action':'/action-delete/<str:pk>',
   }

   return Response(api_urls)


@api_view(['GET'])
def actionList(request):
   budget = Budget.objects.all()
   serializer = BudgetSerializer(budget, many=True)

   return Response(serializer.data)


@api_view(['GET'])
def actionDetail(request, pk):
   budget = Budget.objects.get(id=pk)
   serializer = BudgetSerializer(budget, many=False)

   return Response(serializer.data)


@api_view(['POST'])
def actionCreate(request):
   serializer = BudgetSerializer(data=request.data)

   if serializer.is_valid():
      serializer.save()

   return Response(serializer.data)


@api_view(['PUT'])
def actionUpdate(request, pk):
   budget = Budget.objects.get(id=pk)
   serializer = BudgetSerializer(instance=budget, data=request.data)

   if serializer.is_valid():
      serializer.save()

   return Response(serializer.data)
   

@api_view(['DELETE'])
def actionDelete(request, pk):
   budget = Budget.objects.get(id=pk)
   
   budget.delete()

   return Response("Data berhasil dihapus")


