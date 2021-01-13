from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, "index.html")

def third(request):
    return HttpResponse("test 3 page")

def secom(request):
    return HttpResponse("thisis page3")