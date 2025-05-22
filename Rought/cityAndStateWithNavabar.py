def navbar(request):
    city = None
    state = None

    if request.user.is_authenticated:
        profile = request.user.profile  # ya aapka model
        city = profile.city
        state = profile.state

    return {
        'user_city': city,
        'user_state': state,
    }


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
# from taxi_app.navbar import navbar

def redirect_based_on_location(request):
    context = navbar(request)  # Get city/state
    city = context.get("user_city")
    state = context.get("user_state")
    
    if city and state:
        return redirect(f'home/pin/{city}/{state}/')
    else:
        return redirect('home/location/')

urlpatterns = [
    path('', redirect_based_on_location),  # Root path check
    path('location/', lambda request: redirect('home/location/', permanent=False)),
    path('admin/', admin.site.urls),
    path('home/', include('taxi_app.urls')),
    path('ls/', include('Driver.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
