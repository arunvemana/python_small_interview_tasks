from django.urls import path
from .views import home, user_list,details

urlpatterns = [
    path('', home, name='home'),
    path('users/', user_list, name='userlist'),
    path('details/<trans_id>',details,name='details')
]
