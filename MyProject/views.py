from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse('Welcome to my Project')

def course(request):
    return HttpResponse('Welcome to my Project')

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def homePage(request):
    
    return render(request,"indexx.html")

def userForm(request):
    try:
        n1=request.GET['username']
        n2=request.GET['email']
        n3=request.GET['password']
        print(n1);
    except:
        pass

    return render(request,"userform.html")