from django.shortcuts import render, HttpResponse
from .forms import employee_Form

# Create your views here.


def employeeList(request):
    return render(request, 'employeeRegister/employeeList.html')

def employeeForm(request):
    form = employee_Form()
    return render(request, 'employeeRegister/employeeForm.html', {'form':form})

def employeeDelete(request):
    return render(request, 'base.html')