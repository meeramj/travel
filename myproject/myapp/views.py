from django.http import HttpResponse
from django.shortcuts import render

from .models import Destination
# Create your views here.
def home(request):
    obj=Destination.objects.all()
    return render(request, 'index.html',{'result':obj})


# def operation(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     ares = x + y
#     sres = x - y
#     mres = x * y
#     dres = x / y
#     return render(request, 'result.html', {'addit': ares, 'sub': sres, 'mult': mres, 'divi': dres})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def detail(request):
    return render(request, 'detail.html')


def thanks(request):
    return HttpResponse("Thank you for viewing my page")
