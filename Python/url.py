# added mobile no status of ready for the trip user
# add all security
from django.shortcuts import redirect


# http://localhost:8000/home/otp-testing/
def redirectPathFunctionBaseViews(referrer):
    oldPath = referrer[21:] # remove http://localhost:8000
    listOfTaxiApp = ['home', '', 'location', 'ls']
    listOfTaxi_App = ['in', 'pin', 'status', 'review', 'delete-review', 'otp-testing']

    path = oldPath.strip('/').split('/')
    for i in listOfTaxiApp:
        if oldPath == i:
            ...
    

referrer = 'http://localhost:8000/home/otp-testing/TAXI123/'
redirectPathFunctionBaseViews(referrer=referrer)


# http://127.0.0.1:8000/profile/25/
# noraml with a tag -> no use for function
# <a href="{{ request.META.HTTP_REFERER }}" class="btn btn-outline-dark"> <i class="bi bi-arrow-left"></i> Go Back </a>



# for post method -> redirect
# <form method="POST">
#   {% csrf_token %}
#   <input type="hidden" name="redirect_url" value="{{ request.META.HTTP_REFERER }}">
#   <button type="submit">Submit</button>
# </form>
def form_submit(request):
    if request.method == 'POST':
        redirect_url = request.POST.get('redirect_url', '/')
        return redirect(redirect_url)

