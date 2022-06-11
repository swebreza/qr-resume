from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    
    path('dashboard', views.dashboard,name='dashboard'),
    path('detailedView', views.detailedView,name='detailedView'),
]