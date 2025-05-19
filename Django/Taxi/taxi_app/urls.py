from django.urls import path
from taxi_app import views

app_name = 'taxi_app'

urlpatterns = [
    path('', views.HomePageForTaxiAppViewFunction, name='home'),
    path('review/', views.reviewPageFunctionBaseView, name='review'),
]