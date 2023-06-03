from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_home, name='home'),
    path('CharityGo/ngo/<str:uuid>', views.view_ngo, name="viewngo"),
    path('CharityGo/ngos', views.view_ngos, name='viewngos'),
    path('CharityGo/ngos/search/', views.view_filter_ngos, name='viewfilteredngos'),
    path('CharityGo/aboutus', views.view_aboutus, name='viewaboutus'),
    path('CharityGo/joinus/', views.view_joinus, name='viewjoinus'),
    path('CharityGo/donor/register/', views.view_register_donor, name='registerdonor'),
    path('CharityGo/login', views.view_login, name="login"),
    path('CharityGo/login/validate/', views.validate_user, name="validateuser"),
    path('CharityGo/ngo/dashboard/<str:uuid>', views.view_ngo_dashboard, name='ngodashboard'),
    path('CharityGo/ngo/dashboard/<str:uuid>/logout', views.view_ngo_logout, name='ngologout'),
    path('CharityGo/ngo/<str:ngouuid>/campaign/edit/<str:campaignuuid>', views.view_edit_campaign, name='editcampaign'),
    path('CharityGo/ngo/<str:ngouuid>/campaign/edit/<str:campaignuuid>/save/', views.view_save_edited_campaign, name='saveeditedcampaign'),
    path('CharityGo/ngo/<str:ngouuid>/campaign/delete/<str:campaignuuid>', views.view_delete_campaign, name='deletecampaign'),
    path('CharityGo/ngo/<str:ngouuid>/campaign/add', views.view_add_campaign, name='addcampaign'),
    path('CharityGo/ngo/<str:ngouuid>/campaign/add/save/', views.view_save_added_campaign, name='saveaddedcampaign'),
    path('CharityGo/ngo/<str:ngouuid>/sponsorrequest/edit/<str:requestuuid>', views.view_edit_sponsor_request, name='editsponsorrequest'),
    path('CharityGo/ngo/<str:ngouuid>/sponsorrequest/edit/<str:requestuuid>/save/', views.view_save_edited_sponsor_request, name='saveeditedsponsorrequest'),
    path('CharityGo/ngo/<str:ngouuid>/sponsorrequest/delete/<str:requestuuid>', views.view_delete_sponsor_request, name='deletesponsorrequest'),
    path('CharityGo/ngo/<str:ngouuid>/sponsorrequest/add', views.view_add_sponsor_request, name='addsponsorrequest'),
    path('CharityGo/ngo/<str:ngouuid>/sponsorrequest/add/save/', views.view_save_added_sponsor_request, name='saveaddedsponsorrequest'),
    path('CharityGo/ngo/<str:ngouuid>/sponsorrequest/<str:requestuuid>/reports', views.view_sponsor_request_reports, name='viewsponsorrequestreports'),
    path('CharityGo/donor/dashboard/<str:uuid>', views.view_donor_dashboard, name='donordashboard'),
    path('CharityGo/donor/donate/ngo/<str:ngouuid>/sponsorrequest/<str:requestuuid>/save', views.view_donate_to_sponsor_request_save, name='donatetosponsorrequestsave'),
    path('CharityGo/donor/mydonations', views.view_my_donations, name='mydonations'),
    path('CharityGo/donor/generatepdf', views.generate_pdf, name='generatepdf'),
    path('CharityGo/donor/logout', views.view_donor_logout, name='donorlogout'),

]