from django.shortcuts import render, HttpResponse

# Create your views here.
def HomePageForTaxiAppViewFunction(request):
    return HttpResponse('Welcome to Home Page For Big Taxi App.')