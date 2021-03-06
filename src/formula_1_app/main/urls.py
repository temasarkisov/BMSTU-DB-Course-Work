from django.urls import path

from .views import *

urlpatterns = [
    path('search/', search, name='search'),
    path('user_settings/', user_settings, name='user_settings'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='sign_up')
]