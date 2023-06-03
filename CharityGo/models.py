from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # E.g. 'Edhi Foundation'
    ngo_name = models.CharField(max_length=50, null=False, blank=False)
    # E.g. 'Shahra-e-Faisal, karachi'
    ngo_address = models.CharField(max_length=255, null=False, blank=False)
    # E.g. 'Biggest Ambulance Chaneel In The World'
    ngo_description = models.CharField(max_length=255, null=False, blank=False)
    # E.g. '03285089854'
    ngo_phone = models.CharField(max_length=11, null=False, blank=False)
    # E.g. 'HBL'
    ngo_bank_name = models.CharField(max_length=255, null=False, blank=False)
    # E.g. 'Edhi Foundation'
    ngo_account_title = models.CharField(max_length=255, null=False, blank=False)
    # E.g. 'PK10094999040040'
    ngo_account_no = models.CharField(max_length=255, null=False, blank=False)
    ngo_image = models.ImageField(upload_to="images/", null=False, blank=False)
    # Audit fields
    date_created = models.DateTimeField(default=timezone.now, null=False, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, editable=False, related_name='ngo_creator')
    date_updated = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='ngo_updater')
    voided = models.BooleanField(default=False, null=False)
    date_voided = models.DateTimeField(null=True)
    voided_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='ngo_voider')
    void_reason = models.CharField(null=True, max_length=1024)
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)

    def save(self, created_by=None, *args, **kwargs):
        #Check if user already has an NGO
        ngo = NGO.objects.filter(user=self.user).first()
        if ngo is not None:
            raise Exception('One User Cannot Have Multiple NGOs') 
        #Check if NGO with same name already exists     
        ngo = NGO.objects.filter(ngo_name=self.ngo_name).first()   
        if ngo is not None:
            raise ValueError('NGO Already Exists With Same Name')
        #Check for all required fields 
        if not self.ngo_name:
            raise ValueError('NGO Name Is Required')
        if not self.ngo_address:
            raise ValueError('NGO Address Is Required')
        if not self.ngo_description:
            raise ValueError('NGO Description Is Required')
        if not self.ngo_phone:
            raise ValueError('NGO Phone No. Is Required')
        if not self.ngo_bank_name:
            raise ValueError('NGO Bank Name Is Required')
        if not self.ngo_account_title:
            raise ValueError('NGO Account Title Is Required')
        if not self.ngo_account_no:
            raise ValueError('NGO Account No. Is Required')
        if not self.ngo_image:
            raise ValueError('NGO Image Is Required')
        self.date_created = timezone.now()
        if not created_by:
            created_by = User.objects.get(pk=1)
        self.created_by = created_by
        super().save()

    def update(self, updated_by=None, *args, **kwargs):
        self.date_updated = timezone.now()
        if (not updated_by):
            updated_by = User.objects.get(pk=1)
        self.updated_by = updated_by
        super().save()
    
    def delete(self, voided_by=None, *args, **kwargs):
        self.voided = True
        self.date_voided = timezone.now()
        if (not self.void_reason):
            self.void_reason = 'Voided without providing a reason'
        if (not voided_by):
            voided_by = User.objects.get(pk=1)
        self.voided_by = voided_by
        super().save()
    
    def undelete(self, *args, **kwargs):
        if self.voided:
            self.voided = False
            self.date_voided = None
            self.void_reason = None
            self.voided_by = None
            super().save()
    
    def purge(self, *args, **kwargs):
        super().delete()


class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    donor_name = models.CharField(max_length=50, null=False, blank=False)
    donor_cnic = models.IntegerField(max_length=13, null=False, blank=False)
    # Audit fields
    date_created = models.DateTimeField(default=timezone.now, null=False, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, editable=False, related_name='donor_creator')
    date_updated = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='donor_updater')
    voided = models.BooleanField(default=False, null=False)
    date_voided = models.DateTimeField(null=True)
    voided_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='donor_voider')
    void_reason = models.CharField(null=True, max_length=1024)
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)

    def save(self, created_by=None, *args, **kwargs):
        #Check if user already has a donor account
        donor = Donor.objects.filter(user=self.user).first()
        if donor is not None:
            raise Exception('One User Cannot Have Multiple Donor Accounts')
        #Check for all required fields      
        donor = Donor.objects.filter(donor_name=self.donor_name).first()    
        if donor is not None:
            raise ValueError('NGO Already Exists With Same Name')        
        if not self.donor_name:
            raise ValueError('Donor Name Is Required')
        if not self.donor_cnic:
            raise ValueError('Donor CNIC Is Required')        
        self.date_created = timezone.now()
        if not created_by:
            created_by = User.objects.get(pk=1)
        self.created_by = created_by
        super().save()

    def update(self, updated_by=None, *args, **kwargs):
        self.date_updated = timezone.now()
        if (not updated_by):
            updated_by = User.objects.get(pk=1)
        self.updated_by = updated_by
        super().save()
    
    def delete(self, voided_by=None, *args, **kwargs):
        self.voided = True
        self.date_voided = timezone.now()
        if (not self.void_reason):
            self.void_reason = 'Voided without providing a reason'
        if (not voided_by):
            voided_by = User.objects.get(pk=1)
        self.voided_by = voided_by
        super().save()
    
    def undelete(self, *args, **kwargs):
        if self.voided:
            self.voided = False
            self.date_voided = None
            self.void_reason = None
            self.voided_by = None
            super().save()
    
    def purge(self, *args, **kwargs):
        super().delete()


class Campaign(models.Model):
    campaign_id = models.AutoField(primary_key=True, db_column='id')
    campaign_name = models.CharField(max_length=50, null=False, blank=False)
    campaign_description = models.CharField(max_length=255, null=False, blank=False)
    campaign_image = models.ImageField(upload_to="images/", null=False, blank=False)
    NGO = models.ForeignKey(NGO, null=False, on_delete=models.CASCADE)
    # Audit fields
    date_created = models.DateTimeField(default=timezone.now, null=False, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, editable=False, related_name='campaign_creator')
    date_updated = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='campaign_updater')
    voided = models.BooleanField(default=False, null=False)
    date_voided = models.DateTimeField(null=True)
    voided_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='campaign_voider')
    void_reason = models.CharField(null=True, max_length=1024)
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)

    def save(self, created_by=None, *args, **kwargs): 
        #Check if campaign with same name already exists under an NGO    
        campaigns = Campaign.objects.filter(campaign_name=self.campaign_name).first()    
        if campaigns is not None:
            raise ValueError('Campaign Already Exists With Same Name')
        #Check for all required fields
        if not self.campaign_name:
            raise ValueError('Campaign Name Is Required')
        if not self.campaign_description:
            raise ValueError('Campaign Description Is Required') 
        if not self.campaign_image:
            raise ValueError('Campaign Image Is Required')
        if not self.NGO:
            raise ValueError('NGO Is Required')        
        self.date_created = timezone.now()
        if not created_by:
            created_by = User.objects.get(pk=1)
        self.created_by = created_by
        super().save()

    def update(self, updated_by=None, *args, **kwargs):
        self.date_updated = timezone.now()
        if (not updated_by):
            updated_by = User.objects.get(pk=1)
        self.updated_by = updated_by
        super().save()
    
    def delete(self, voided_by=None, *args, **kwargs):
        self.voided = True
        self.date_voided = timezone.now()
        if (not self.void_reason):
            self.void_reason = 'Voided without providing a reason'
        if (not voided_by):
            voided_by = User.objects.get(pk=1)
        self.voided_by = voided_by
        super().save()
    
    def undelete(self, *args, **kwargs):
        if self.voided:
            self.voided = False
            self.date_voided = None
            self.void_reason = None
            self.voided_by = None
            super().save()
    
    def purge(self, *args, **kwargs):
        super().delete()


class SponsorRequest(models.Model):
    request_id = models.AutoField(primary_key=True, db_column='id')
    request_name = models.CharField(max_length=50, null=False, blank=False)
    request_description = models.CharField(max_length=255, null=False, blank=False)
    request_image = models.ImageField(upload_to="images/", null=False, blank=False)
    request_price = models.IntegerField(null=False, blank=False)
    NGO = models.ForeignKey(NGO, null=False, on_delete=models.CASCADE)
    # Audit fields
    date_created = models.DateTimeField(default=timezone.now, null=False, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, editable=False, related_name='request_creator')
    date_updated = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='request_updater')
    voided = models.BooleanField(default=False, null=False)
    date_voided = models.DateTimeField(null=True)
    voided_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='request_voider')
    void_reason = models.CharField(null=True, max_length=1024)
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)

    def save(self, created_by=None, *args, **kwargs):   
        #Check if Sponsor Request with same name already exists under an NGO    
        sponsor_requests = SponsorRequest.objects.filter(request_name=self.request_name).first()    
        if sponsor_requests is not None:
            raise ValueError('Request Already Exists With Same Name')
        #Check for all required fields
        if not self.request_name:
            raise ValueError('Request Name Is Required')
        if not self.request_description:
            raise ValueError('Request Description Is Required') 
        if not self.request_image:
            raise ValueError('Request Image Is Required')
        if not self.request_price:
            raise ValueError('Request Price Is Required')
        if not self.NGO:
            raise ValueError('NGO Is Required')            
        self.date_created = timezone.now()
        if not created_by:
            created_by = User.objects.get(pk=1)
        self.created_by = created_by
        super().save()

    def update(self, updated_by=None, *args, **kwargs):
        self.date_updated = timezone.now()
        if (not updated_by):
            updated_by = User.objects.get(pk=1)
        self.updated_by = updated_by
        super().save()
    
    def delete(self, voided_by=None, *args, **kwargs):
        self.voided = True
        self.date_voided = timezone.now()
        if (not self.void_reason):
            self.void_reason = 'Voided without providing a reason'
        if (not voided_by):
            voided_by = User.objects.get(pk=1)
        self.voided_by = voided_by
        super().save()
    
    def undelete(self, *args, **kwargs):
        if self.voided:
            self.voided = False
            self.date_voided = None
            self.void_reason = None
            self.voided_by = None
            super().save()
    
    def purge(self, *args, **kwargs):
        super().delete()


class Donation(models.Model):
    donation_id = models.AutoField(primary_key=True, db_column='id')
    SponsorRequest = models.ForeignKey(SponsorRequest, null=False, on_delete=models.CASCADE)
    Donor = models.ForeignKey(Donor, null=False, on_delete=models.CASCADE)
    # Audit fields
    date_created = models.DateTimeField(default=timezone.now, null=False, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, editable=False, related_name='donation_creator')
    date_updated = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='donation_updater')
    voided = models.BooleanField(default=False, null=False)
    date_voided = models.DateTimeField(null=True)
    voided_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='donation_voider')
    void_reason = models.CharField(null=True, max_length=1024)
    uuid = models.UUIDField(default=uuid4, editable=False, unique=True)

    def save(self, created_by=None, *args, **kwargs):   
        #Check for all required fields                  
        if not self.SponsorRequest:
            raise ValueError('Sponsor Request Is Required') 
        if not self.Donor:
            raise ValueError('Donor Is Required')            
        self.date_created = timezone.now()
        if not created_by:
            created_by = User.objects.get(pk=1)
        self.created_by = created_by
        super().save()

    def update(self, updated_by=None, *args, **kwargs):
        self.date_updated = timezone.now()
        if (not updated_by):
            updated_by = User.objects.get(pk=1)
        self.updated_by = updated_by
        super().save()
    
    def delete(self, voided_by=None, *args, **kwargs):
        self.voided = True
        self.date_voided = timezone.now()
        if (not self.void_reason):
            self.void_reason = 'Voided without providing a reason'
        if (not voided_by):
            voided_by = User.objects.get(pk=1)
        self.voided_by = voided_by
        super().save()
    
    def undelete(self, *args, **kwargs):
        if self.voided:
            self.voided = False
            self.date_voided = None
            self.void_reason = None
            self.voided_by = None
            super().save()
    
    def purge(self, *args, **kwargs):
        super().delete()





    
