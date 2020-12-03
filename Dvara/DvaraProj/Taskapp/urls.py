from django.urls import path
from .views import Home, sub_category_list

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('ajax/sub_category_list/', sub_category_list,
         name='sub_category_list'),
]
