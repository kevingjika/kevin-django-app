from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name="home"),
        path('aboutus/', views.aboutus, name="aboutus"),
        path('contactus/', views.contactus, name="contactus"),
        path('iphone6/', views.iphone6, name="iphone6"),
        path('iphone6plus/', views.iphone6plus, name="iphone6plus"),
        path('iphone14promax/', views.iphone14promax, name="iphone14promax"),
        path('se1100/', views.se1100, name="se1100"),
        path('sga12/', views.sga12, name="sga12"),
        path('sgs22ultra/', views.sgs22ultra, name="sgs22ultra"),
        path('iphone11/', views.iphone11, name="iphone11"),
        path('iphone12/', views.iphone12, name="iphone12"),
        path('iphone13/', views.iphone13, name="iphone13"),
        path('sgs6/', views.sgs6, name="sgs6"),
        path('sgs6e/', views.sgs6e, name="sgs6e"),
        path('sgs6ep/', views.sgs6ep, name="sgs6ep"),
        path('register/', views.register, name="register"),
        path('login/', views.login, name="login"),
        path('logout/', views.logout, name="logout"),
        ]