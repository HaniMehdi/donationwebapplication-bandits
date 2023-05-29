from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.urls import reverse
from django.db.models import Q
from CharityGo.models import NGO, Campaign
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
    return HttpResponse('Login')


def validate_user(request):
    return HttpResponse('Validate')
    
    
def view_ngo_dashboard(request, uuid):
    return HttpResponse('Dashboard')
    
            
        