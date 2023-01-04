from django.urls import path,include
from  rest_framework.authtoken.views import obtain_auth_token

from .views import BuyerRegisterApiView,SenderRegisterApiView

urlpatterns = [
    path('register/sender/', SenderRegisterApiView.as_view()),
    path('register/buyer/', BuyerRegisterApiView.as_view()),
    path('token/',obtain_auth_token)
]