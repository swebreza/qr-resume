from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    
    path('detailedView/<int:id>', views.detailedView,name='detailedView'),
]