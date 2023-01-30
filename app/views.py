from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def form(request):
    if request.method=='get':
        un=request.POST['username']
        pw=request.POST['password']
        print(un)
        print(pw)
        return HttpResponse('Data is submiited!!')

    return render(request,'form.html')

def forms(request):
    if request.method=='POST':
        un=request.POST['username']
        pw=request.POST['password']
        print(un)
        print(pw)
        return HttpResponse('Data is submiited!!')

    return render(request,'forms.html')