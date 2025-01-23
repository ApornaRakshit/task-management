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


# def create_task(request):
#     form = TaskForm(employees = {"name":"John", "id": 1})
#     context = {"form": form}
#     return render(request, "task_form.html", context)




# from django.shortcuts import render
# from tasks.forms import TaskForm
# # from django.http import HttpResponse

# # Create your views here.

# # def home(request):
# #     return HttpResponse("Welcome to the task management system")

# def manager_dashboard(request):
#     return render(request, "dashboard/manager-dashboard.html")


# def user_dashboard(request):
#     return render(request, "dashboard/user-dashboard.html")

# def test(request):
#     context = {                 #  declaring a dictionary
#         "names" : ['Sam', 'Tiara', 'John'],
#         "age" : 23
#     }
#     return render(request, "test.html", context)


# def create_task(request):
#     form = TaskForm(employees = {"name":"John", "id": 1})
#     context = {"form": form}
#     return render(request, "task_form.html", context)
