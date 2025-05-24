from django.contrib import admin
from Users.models import usersDataModel, ReviewAndRating, ReviewBarcode
# Register your models here.

admin.site.register(usersDataModel)
admin.site.register(ReviewAndRating)
admin.site.register(ReviewBarcode)