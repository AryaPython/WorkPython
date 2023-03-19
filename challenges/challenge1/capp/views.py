from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo1(request):
    return HttpResponse("My homepage")
def homepage(request):
    return render(request,"homepage.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return HttpResponse("here are the list")
def details(request):
    return render(request,"details.html")
def thanks(request):
    return HttpsResponse("thanks for reading")