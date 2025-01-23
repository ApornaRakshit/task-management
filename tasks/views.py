from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

<<<<<<< HEAD

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    context = {
        "name" : ["Mars", "Aps", "Bushri", "Soi"],
        "age": 23
    }
    return render(request, 'test.html', context)
=======
def show_task(request):
    return HttpResponse("This is our task page")

def show_specific_task(request,id):
    print("id",id)
    print("id type", type(id))
    return HttpResponse("This is specific task page{id}")
>>>>>>> dynamic_urls
