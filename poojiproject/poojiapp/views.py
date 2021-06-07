from django.shortcuts import render
from poojiapp.forms import studentform
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'homepage.html')

# def studentreg(request):
#     form =studentform()
#     if request.method =="POST":
#         form =studentform(request.POST)
#         if form.is_valid():
#             form.save(commit =True)
#
#             return index(request)
#         else:
#             print("sorry!")
#     return render(request,'formpage.html',{"form":form})

def studentreg(request):
    form =studentform()
    if request.method =="POST":
        form =studentform(request.POST)
        if form.is_valid():
             form.save(commit=True)

             return render(request,'finalpage.html')
        else:
            print("ERROR INVALID!!!!!")
    return render(request,'formpage.html',{"form":form})
