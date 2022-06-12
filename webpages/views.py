from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
 return render (request,'webpages/index.html')





def detailedView(request,id):
 return render (request,'webpages/detailedView.html')