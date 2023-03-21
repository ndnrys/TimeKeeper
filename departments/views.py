from django.shortcuts import render
from app.models import Departments

def list(request):
    context = {
        'departments_list': Departments.objects.all(),
    }
    return render(request, 'app/departments/list.html', context)