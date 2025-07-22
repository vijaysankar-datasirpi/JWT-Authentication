from django.urls import path
from .views import UserSignUp,UserLogIn,UserProfileView,UserPasswordView

urlpatterns=[
    path('insert',UserSignUp.as_view(),name='insert'),
    path('check',UserLogIn.as_view(),name='check'),
    path('getprofile',UserProfileView.as_view(),name='getprofile'),
    path('getusername',UserPasswordView.as_view(),name='getusername')
]