from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userForms

def aboutUs(request):
    return HttpResponse('Welcome to my Project')

def course(request):
    return HttpResponse('Welcome to my Project')

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def homePage(request):
    
    return render(request,"indexx.html")

def userForm(request):
    fn=userForms()

    try:
        n1=request.POST['username']
        n2=request.POST['email']
        n3=request.POST['password']
        output = print(n1);
    
    #    return HttpResponseRedirect('/about-us/')
    except:
        pass

    return render(request,"userform.html")

def submitform(request):
    return HttpResponse(request)
