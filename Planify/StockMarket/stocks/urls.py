from django.urls import path
from .views import test, form
urlpatterns = [
    path('test/',test),
    path('form/',form,name="form")
]
