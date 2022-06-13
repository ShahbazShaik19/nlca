import re
from django.http import HttpResponse
from django.shortcuts import render
from nlca_app.nlca_modules.encript import encript
from nlca_app.nlca_modules.encryption import encryption


# Create your views here.
def home(request):
    return render(request, "home.html")

def encr(request):
    pt = request.POST["pt"]
    key = request.POST["key"]
    try:
        pt,kk1,kk2,kk3,kk4,kkk,ct = encryption()
        return render(request, "home.html", {"display" : "block", "pt": pt, "kk1":kk1, "kk2":kk2, "kk3":kk3, "kk4":kk4, "kkk":kkk, "ct":ct})
        # res= encryption()
        # return render(request, "encryption.html", {"result": res})
    except Exception as e:
        return HttpResponse("<h1>Input Error Occurred!<h1><h2>Error Message: <h2>" + str(e))
