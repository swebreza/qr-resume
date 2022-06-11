from django.shortcuts import render
# Create your views here.

def index(request):
 return render (request,'webpages/index.html')

def signup(request):
 return render (request,'webpages/signup.html')

def login(request):
 return render (request,'webpages/login.html')


def dashboard(request):
 return render (request,'webpages/dashboard.html')

def detailedView(request):
 return render (request,'webpages/detailedView.html')