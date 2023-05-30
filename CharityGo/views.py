from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.urls import reverse
from django.db.models import Q
from CharityGo.models import NGO, Campaign
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth

# Create your views here.

def view_home(request):
    template = loader.get_template('home.html')
    ngos = NGO.objects.filter(voided=False).order_by('ngo_name')
    campaigns = Campaign.objects.filter(voided=False).order_by('campaign_name')
    for ngo in ngos:
          if len(ngo.ngo_description) > 150:
               ngo.ngo_description = ngo.ngo_description[0:151] + ' ...'
    context = {
        'navbar': 'home',
        'ngos' : ngos,
        'campaigns' : campaigns
    }
    return HttpResponse(template.render(context, request))


def view_ngo(request, uuid):
    template = loader.get_template('ngo.html')
    ngo = NGO.objects.filter(uuid=uuid).first()
    campaigns = Campaign.objects.filter(voided=False, NGO=ngo).order_by('campaign_name')
    context = {
        'navbar': 'ngos',
        'ngo' : ngo,
        'campaigns' : campaigns
    }
    return HttpResponse(template.render(context, request))


def view_ngos(request):
     template = loader.get_template('ngos.html')
     ngos = NGO.objects.all().order_by('ngo_name')
     for ngo in ngos:
          if len(ngo.ngo_description) > 150:
               ngo.ngo_description = ngo.ngo_description[0:151] + ' ...'
     context = {
          'navbar' : 'ngos',
          'ngos' : ngos,
     }
     return HttpResponse(template.render(context, request))


def view_aboutus(request):
     template = loader.get_template('aboutus.html')
     context = {
          'navbar' : 'aboutus',
     }
     return HttpResponse(template.render(context, request))


def view_joinus(request):
     template = loader.get_template('joinus.html')
     _ngoemail = request.POST.get('email')     
     if request.method == 'POST' and _ngoemail:
          _password = request.POST.get('password')
          _repassword = request.POST.get('re-password')
          if _password != _repassword:          
               context = {
                    'navbar' : 'joinus',
                    'error' : 'Both Passwords Do Not Match'
               }
               return HttpResponse(template.render(context, request))          
          _ngoname = request.POST.get('ngo_name')
          _ngoaddress = request.POST.get('ngo_address')
          _ngodescription = request.POST.get('ngo_description')
          _ngophone = request.POST.get('ngo_phone')
          _ngobankname = request.POST.get('ngo_bank_name')
          _ngoaccounttitle = request.POST.get('ngo_account_title')
          _ngoaccountno = request.POST.get('ngo_account_no')
          _ngoimage = request.FILES.get('ngo_image')      
          user = User.objects.create_superuser(
               username=_ngoname.replace(' ', '-'), 
               password=_password, 
               email=_ngoemail
            )
          NGO.objects.create(
               user=user, 
               ngo_name=_ngoname, 
               ngo_address=_ngoaddress, 
               ngo_description=_ngodescription, 
               ngo_phone=_ngophone, 
               ngo_bank_name=_ngobankname, 
               ngo_account_title=_ngoaccounttitle, 
               ngo_account_no=_ngoaccountno, 
               ngo_image=_ngoimage, 
               created_by=user
            ).save()
          return redirect('login')
     context = {
          'navbar' : 'joinus',
     }
     return HttpResponse(template.render(context, request))


def view_login(request, message=None):
    if request.user.is_authenticated:
                    ngo = NGO.objects.filter(user = request.user).first()
                    return redirect('ngodashboard', uuid=ngo.uuid)
    template = loader.get_template('login.html')
    context = {
        'navbar': 'login',
        'error' : message
    }
    return HttpResponse(template.render(context, request))


def validate_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()
        if user is not None:
            if user.check_password(password):
                login(request, user)
                return redirect('login')
        request.error = 'Invalid Email or Password'
        return view_login(request, 'Invalid Email or Password')
    return redirect('login')
    
    
def view_ngo_dashboard(request, uuid):
    template = loader.get_template('ngo_dashboard.html')
    ngo = NGO.objects.filter(uuid=uuid).first()
    campaigns = Campaign.objects.filter(NGO=ngo, voided=False).order_by('campaign_name')
    context = {
         'ngo' : ngo,
         'campaigns' : campaigns,
    }
    return HttpResponse(template.render(context, request))


def view_ngo_logout(request, uuid):
     auth.logout(request)
     return redirect('home')


def view_edit_campaign(request, ngouuid, campaignuuid):
     template = loader.get_template('edit_campaign.html')
     ngo = NGO.objects.filter(uuid=ngouuid).first()
     campaign = Campaign.objects.filter(uuid=campaignuuid).first()
     context = {
          'ngo' : ngo,
          'campaign' : campaign,
     }
     return HttpResponse(template.render(context, request))


def view_save_edited_campaign(request, ngouuid, campaignuuid):
     if request.method == 'POST':
          _campaignname = request.POST.get('campaign_name')
          _campaigndescription = request.POST.get('campaign_description')
          _campaignimage = request.FILES.get('campaign_image') 
          print(_campaignimage)                   
          ngo = NGO.objects.filter(uuid=ngouuid).first()
          campaign = Campaign.objects.filter(uuid=campaignuuid).first()
          campaign.campaign_name = _campaignname
          campaign.campaign_description = _campaigndescription
          campaign.updated_by = ngo.user
          if _campaignimage is not None:               
               campaign.campaign_image = _campaignimage               
          campaign.update();
          return redirect('login')


def view_delete_campaign(request, ngouuid, campaignuuid):
     ngo = NGO.objects.filter(uuid=ngouuid).first()
     campaign = Campaign.objects.filter(uuid=campaignuuid).first()
     campaign.voided_by = ngo.user
     campaign.delete()
     return redirect('login')


def view_add_campaign(request, ngouuid):
     template = loader.get_template('add_campaign.html')
     ngo = NGO.objects.filter(uuid=ngouuid).first()
     context ={
          'ngo' : ngo
     }
     return HttpResponse(template.render(context, request))


def view_save_added_campaign(request, ngouuid):
     if request.method == "POST":
          _campaignname = request.POST.get('campaign_name')
          _campaigndescription = request.POST.get('campaign_description')
          _campaignimage = request.FILES.get('campaign_image')
          ngo = NGO.objects.filter(uuid=ngouuid).first()
          Campaign.objects.create(campaign_name = _campaignname, campaign_description = _campaigndescription, campaign_image = _campaignimage,
                                  NGO = ngo, created_by = ngo.user).save()
          return redirect('login')



    
            
        