from django.shortcuts import render, get_object_or_404, redirect
from app.models import Departments

def list(request):
    context = {
        'departments_list': Departments.objects.all(),
        'method': test()
    }
    return render(request, 'app/departments/list.html', context)

def test():
    return "関数を使ってます"

def detail(request, pk):
    departments = get_object_or_404(Departments, pk=pk)
    return render(request, 'app/departments/detail.html', {'departments': departments})

def new(request):
    pass

def edit(request, pk):
    pass