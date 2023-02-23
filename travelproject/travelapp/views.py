from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"index.html")
def sachu(request):
    return render(request,"sachu.html")
def mino(request):
    return HttpResponse("mino how are you")
