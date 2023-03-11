from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('addtask',views.addtask, name='addtask'),
    path('update/<str:name>',views.update, name="update"),
    path('delete/<str:name>',views.delete, name="delete"),
    path('update/<str:name>/update',views.update, name="update"),

]
