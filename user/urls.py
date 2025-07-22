from django.urls import path
from .views import UserSignUp,UserLogIn,UserView

urlpatterns=[
    path('insert',UserSignUp.as_view(),name='insert'),
    path('check',UserLogIn.as_view(),name='check'),
    path('gettoken',UserView.as_view(),name='gettoken'),
] 