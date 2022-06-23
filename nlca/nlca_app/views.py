#import re
from django.http import HttpResponse
from django.shortcuts import render
from nlca_app.nlca_modules.ascii import atoh
from nlca_app.nlca_modules.decryption import decryption
from nlca_app.nlca_modules.encryption import encryption


# Create your views here.
def home(request):
    return render(request, "home.html")

def encryption_home(request):
    return render(request, "encryption.html")

def decryption_home(request):
    return render(request, "decryption.html")

def decr_home(request):
    ct1 = request.POST["ct"]
    key1 = request.POST["key"]
    return render(request, "decryption.html",{"ct1":ct1, "key1":key1})

def encr(request):
    pt = request.POST["pt"]
    key = request.POST["key"]
    try:
        kk1,kk2,kk3,kk4,kkk,ct = encryption(pt,key)
        kk1,kk2,kk3,kk4,kkk,pt_d, pt_ascii,time = decryption(ct,key)
        pt2=""
        pt_hex=atoh(pt)
        for i in range(0,len(pt_hex),2):
            pt2=pt2+pt_hex[i:i+2]+" "
        key2=""
        for i in range(0,len(key),2):
            key2=key2+key[i:i+2]+" "
        ct2=""
        for i in range(0,len(ct),2):
            ct2=ct2+ct[i:i+2]+" "
        return render(request, "encryption.html", {"display" : "inline-block", "pt":pt, "pt2": pt2, "key2":key2, "kk1":kk1, "kk2":kk2, "kk3":kk3, "kk4":kk4, "kkk":kkk, "ct2":ct2, "ptd":pt_d, "pt_ascii": pt_ascii, "time":time})
        # res= encryption()
        # return render(request, "encryption.html", {"result": res})
    except Exception as e:
        return HttpResponse("<h1>Input Error Occurred!<h1><h2>Error Message: <h2>" + str(e))

# def decr(request):
#     pt = request.POST["pt"]
#     key = request.POST["key"]
#     try:
#         kk1,kk2,kk3,kk4,kkk,ct = decryption(pt,key)
#         pt2=""
#         for i in range(0,len(pt),2):
#             pt2=pt2+pt[i:i+2]+" "
#         return render(request, "decryption.html", {"display" : "block", "pt": pt2, "kk1":kk1, "kk2":kk2, "kk3":kk3, "kk4":kk4, "kkk":kkk, "ct":ct})
#         # res= encryption()
#         # return render(request, "encryption.html", {"result": res})
#     except Exception as e:
#         return HttpResponse("<h1>Input Error Occurred!<h1><h2>Error Message: <h2>" + str(e))
