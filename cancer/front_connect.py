from cgi import test
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def home2(request):
    
    return render(request,'home2.html')

def home3(request):
    return render(request,'home3.html')

def testing(request):
    print (request.POST)
    request.POST.get('male')
    return render(request,'testing.html')

