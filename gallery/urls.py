from django.urls import path
from gallery import views
from .views import contactus

app_name = "gallery"
urlpatterns=[
    path('', views.home, name="home"),
    path('shop/', views.shop, name="shop"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('cart/', views.cart, name='cart'),
    path('contactus/', views.contactus, name="contactus"),



    # path('<int:id>', views.gallery_detail, name="gallery_detail"),
]
