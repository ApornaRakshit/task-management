from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")


def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    context = {
        "name" : ["Mars", "Aps", "Bushri", "Soi"],
        "age": 23
    }
    return render(request, 'test.html', context)