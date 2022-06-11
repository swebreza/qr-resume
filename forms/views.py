from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Form
# Create your views here.

def form(request):
 if request.method=='POST':
  first_name=request.POST['firstname']
  last_name=request.POST['lastname']
  objective=request.POST['objective']
  projects=request.POST['projects']
  skills=request.POST['skills']
  location=request.POST['location']
  regards=request.POST['regards']
  # resumeTemplate=request.POST['resumeTemplate']

  formData=Form(first_name=first_name,last_name=last_name,objective=objective,projects=projects,skills=skills,location=location,regards=regards,)
  formData.save()
  messages.success(request,'Successfully submitted')
  return redirect ('dashboard')
 return render(request,'webpages/form.html')