from django.urls import path,include
from poojiapp import views


urlpatterns =[
    path('',views.studentreg, name='studentreg')
]
