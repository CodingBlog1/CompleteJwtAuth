from django.urls import path,include
from .views import UserRegistrationView,UserLoginView,UserChangePasswordView,SendPasswordRestEmailView,UserPasswordRestView

urlpatterns = [
path('register/',UserRegistrationView.as_view(),name='register'),
path('login/',UserLoginView.as_view(),name='login'),
path('changepassword/',UserChangePasswordView.as_view(),name='changepassword'),
path('sendresetpasswordemail/',SendPasswordRestEmailView.as_view(),name='sendresetpasswordemail'),
path('reset-password/<uid>/<token>/',UserPasswordRestView.as_view(),name='sendresetpasswordemail'),

]
