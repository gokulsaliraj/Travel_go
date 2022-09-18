from django.http import HttpResponse
from django.shortcuts import render
from . models import Places,Member


# Create your views here.
def demo(request):
    obj=Places.objects.all()
    obj2=Member.objects.all()

    return render(request, "index.html",{'result':obj,'team':obj2})


"""def result(request):
    a=int(request.GET['num1'])
    b=int(request.GET['num2'])
    add=a+b
    mult=a*b
    sub=a-b
    div=a/b
    return render(request,"result.html",{'add':add,'mult':mult,'sub':sub,'div':div})"""
