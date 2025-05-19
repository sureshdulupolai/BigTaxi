from django.shortcuts import render, HttpResponse

# Create your views here.
def HomePageForTaxiAppViewFunction(request):
    return render(request, 'main/home.html')

def reviewPageFunctionBaseView(request):
    return HttpResponse('review page')