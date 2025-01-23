from django.urls import path
<<<<<<< HEAD
from tasks.views import manager_dashboard,user_dashboard, test

urlpatterns = [
    path('manager-dashboard/', manager_dashboard),
    path('user-dashboard/', user_dashboard),
    path('test/',test)
=======
from tasks.views import show_task,show_specific_task

urlpatterns = [
    path('show_task/',show_task),
    path('show_task/<int:id>/',show_specific_task)
>>>>>>> dynamic_urls
]