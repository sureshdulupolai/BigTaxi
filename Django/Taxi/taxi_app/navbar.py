from django.contrib.auth.models import User
from Users.models import usersDataModel
from django.contrib import messages

def navbar(request):
    if request.user.is_authenticated: 
        checkUser = User.objects.get(username = request.user.username); UDM = usersDataModel.objects.get(ULink = checkUser); 
        userCategoryis = UDM.UserCategory
        userBarCodeAccessis = UDM.UserCode
        userCouponCodeis = UDM.CouponCode
        return {'userCategoryis' : userCategoryis, 'userBarCodeAccessis' : userBarCodeAccessis}
    
    else:
        return {'userCategoryis' : None, 'userBarCodeAccessis' : None}