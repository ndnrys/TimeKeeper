from django.shortcuts import render

def list(request):
    return render(request, 'app/departments/list.html', {'name': '部署管理'})