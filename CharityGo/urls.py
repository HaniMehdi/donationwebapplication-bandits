from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_home, name='home'),
    path('CharityGo/ngo/<str:uuid>', views.view_ngo, name="viewngo"),
    path('CharityGo/ngos', views.view_ngos, name='viewngos'),
    path('CharityGo/aboutus', views.view_aboutus, name='viewaboutus'),
    path('CharityGo/joinus/', views.view_joinus, name='viewjoinus'),
    path('CharityGo/login', views.view_login, name="login"),
    path('CharityGo/login/validate/', views.validate_user, name="validateuser"),
    path('CharityGo/Dashboard/<str:uuid>', views.view_ngo_dashboard, name='ngodashboard'),
]