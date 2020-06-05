from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard_budget"),
    path('update/<str:pk>', views.actionUpdateFrontEnd, name="action_update_frontend"),
    path('detail/<str:pk>', views.actionDetailPerMonth, name="action_detail"),

    path('api/', views.apiOverview, name="api_overview"),
    path('api/action-list/', views.actionList, name="action-list"),
    path('api/action-detail/<str:pk>/', views.actionDetail, name="action-detail"),
    path('api/action-create/', views.actionCreate, name="action_create"),
    path('api/action-update/<str:pk>', views.actionUpdate, name="action_update"),
    path('api/action-delete/<str:pk>', views.actionDelete, name="action_delete"),
   ]