from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myApp.models import *


# Create your views here.

def index(request):
    return render(request,"index.html")


def test(request):
    q= request.GET.get("q")
    return HttpResponse(f"hello {q}")

def country(request):
    country=Country.objects.all()
    return JsonResponse({"data":list(country.values())})

def state(request):
    cid=request.GET.get("cid")
    state=State.objects.filter(country_id=cid)
    return JsonResponse({"data":list(state.values())})

def city(request):
    sid=request.GET.get("sid")
    city=City.objects.filter(state_id=sid)
    return JsonResponse({"data":list(city.values())})