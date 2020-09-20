from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import EmployeeManager


def index(request):
    var = EmployeeManager.objects.all()
    _temp_var = []
    for i in var:
        _temp_var.append({'emp_id':i.id,
                        'emp_name':i.first_name+' '+i.last_name,
                        'manager_name':f"{(i.manager if i.manager else 'CEO')}"})
                         # f string for ' because its return str with out '
    print(_temp_var)
    return JsonResponse(_temp_var, safe=False)
