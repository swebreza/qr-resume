from django.shortcuts import render
# Create your views here.

def index(request):
 return render (request,'webpages/index.html')




def dashboard(request):
 return render (request,'webpages/dashboard.html')

def detailedView(request):
 return render (request,'webpages/detailedView.html')