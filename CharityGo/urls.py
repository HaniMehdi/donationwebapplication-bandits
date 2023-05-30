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
    path('CharityGo/ngo/dashboard/<str:uuid>', views.view_ngo_dashboard, name='ngodashboard'),
    path('CharityGo/ngo/dashboard/<str:uuid>/logout', views.view_ngo_logout, name='ngologout'),
    path('CharityGo/ngo/<str:ngouuid>/campaign/edit/<str:campaignuuid>', views.view_edit_campaign, name='editcampaign'),
    path('CharityGo/ngo/<str:ngouuid>/campaign/edit/<str:campaignuuid>/save/', views.view_save_edited_campaign, name='saveeditedcampaign'),
    path('CharityGo/ngo/<str:ngouuid>/campaign/delete/<str:campaignuuid>', views.view_delete_campaign, name='deletecampaign'),
    path('CharityGo/ngo/<str:ngouuid>/campaign/add', views.view_add_campaign, name='addcampaign'),
    path('CharityGo/ngo/<str:ngouuid>/campaign/add/save/', views.view_save_added_campaign, name='saveaddedcampaign'),
]