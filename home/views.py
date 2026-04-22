from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from home.models import Department, Doctors







def home(request):
  return render(request, 'home.html')
  

def about(request):
   return render(request, 'about.html')
    
def contact(request):
     return render(request, 'contact.html')

def departments(request):
    dict_dept={
'dept':Department.objects.all()
}
    return render(request, 'departments.html',dict_dept)


def doctors(request):
    doctors_list = Doctors.objects.all()
    return render(request, 'doctors.html', {'doctors': doctors_list})

def booking(request):
     return render(request, 'booking.html')