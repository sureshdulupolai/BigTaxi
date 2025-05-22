from django.contrib.auth.models import User
from Users.models import usersDataModel
from django.contrib import messages

def navbar(request):
    if request.user.is_authenticated: 
        checkUser = User.objects.get(username = request.user.username); UDM = usersDataModel.objects.get(ULink = checkUser); 
        userCategoryis = UDM.UserCategory
        userBarCodeAccessis = UDM.UserCode
        userModelDataCityis = UDM.UserCity
        userModelDataStateis = UDM.UserState
        return {'userCategoryis' : userCategoryis, 'userBarCodeAccessis' : userBarCodeAccessis, 'userModelDataCityis' : userModelDataCityis, 'userModelDataStateis' : userModelDataStateis}
    
    else:
        return {'userCategoryis' : None, 'userBarCodeAccessis' : None,  'userModelDataCityis' : None, 'userModelDataStateis' : None}