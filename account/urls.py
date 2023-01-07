from django.urls import path,include
from  rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('register/sender/', views.SenderRegisterApiView.as_view()),
    path('register/buyer/', views.BuyerRegisterApiView.as_view()),
    path('token/',obtain_auth_token)
]