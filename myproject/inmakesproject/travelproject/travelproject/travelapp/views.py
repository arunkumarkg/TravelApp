from django.http import HttpResponse
from django.shortcuts import render
from .models import place, team


# Create your views here.
# def demo(request):


# return render(request, "index.html", {'result': obj,})


def demo(request):
    obj = place.objects.all()
    obj1 = team.objects.all()

    return render(request, "index.html", {'result': obj, 'result1': obj1})
#
# def about (request):
#     return render(request,"about.html")
#
# def contact (request):
#     return HttpResponse("hello am contact")
