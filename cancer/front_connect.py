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
    # print (request.POST)
    checkbox ="" #Variable for gender

    if(request.method == "POST"):
        if(request.POST.get('male') == 1):
            checkbox = 'male'
        elif(request.POST.get('female') == 1):
            checkbox = 'female'
        
        startingAge = request.POST.get('startingAge')
        endingAge = request.POST.get('endingAge')
        startingYear = request.POST.get('startingYear')
        endingYear = request.POST.get('endingYear')

        years = int(endingYear) - int(startingYear)
        age = int(endingAge) - int(startingAge)

        print("age ", age)
        print("years " , years)
        if(checkbox != ""):
            print("Gender: " , checkbox)

        
        # print(years)



    return render(request,'testing.html')

