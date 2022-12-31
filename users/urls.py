from django.urls import path
from .views import UserRegisterView
from .views import *
from . import views


app_name = "users"
urlpatterns=[
    path('register/', UserRegisterView.as_view(), name='register'),
    path('register/', UserRegisterView, name='register'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register')



    # path('<int:id>', views.gallery_detail, name="gallery_detail"),
]
