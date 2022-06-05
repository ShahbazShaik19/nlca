from django.http import HttpResponse
from django.shortcuts import render
from .nlca_modules.encript import encript

# Create your views here.
def home(request):
    return render(request, "home.html")

def encr(request):
    pt = request.POST["pt"]
    key = request.POST["key"]
    try:
        res = encript(pt,key)
        return render(request, "encryption.html", {"result": res})
    except Exception as e:
        return HttpResponse("<h1>Input Error Occurred!<h1><h2>Error Message: <h2>" + str(e))
