from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ngo_name = models.CharField(max_length=50, null=False, blank=False)
    ngo_address = models.CharField(max_length=255, null=False, blank=False)
    ngo_description = models.CharField(max_length=255, null=False, blank=False)
    ngo_phone = models.CharField(max_length=11, null=False, blank=False)
    ngo_bank_name = models.CharField(max_length=255, null=False, blank=False)
    ngo_account_title = models.CharField(max_length=255, null=False, blank=False)
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

    def update(self, updated_by=None, *args, **kwargs):
        self.date_updated = timezone.now()
        if (not updated_by):
            updated_by = User.objects.get(pk=1)
        self.updated_by = updated_by
        self.save()
    
    def delete(self, voided_by=None, *args, **kwargs):
        self.voided = True
        self.date_voided = timezone.now()
        if (not self.void_reason):
            self.void_reason = 'Voided without providing a reason'
        if (not voided_by):
            voided_by = User.objects.get(pk=1)
        self.voided_by = voided_by
        self.save()
    
    def undelete(self, *args, **kwargs):
        if self.voided:
            self.voided = False
            self.date_voided = None
            self.void_reason = None
            self.voided_by = None
            self.save()
    
    def purge(self, *args, **kwargs):
        self.delete()


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

    def update(self, updated_by=None, *args, **kwargs):
        self.date_updated = timezone.now()
        if (not updated_by):
            updated_by = User.objects.get(pk=1)
        self.updated_by = updated_by
        self.save()
    
    def delete(self, voided_by=None, *args, **kwargs):
        self.voided = True
        self.date_voided = timezone.now()
        if (not self.void_reason):
            self.void_reason = 'Voided without providing a reason'
        if (not voided_by):
            voided_by = User.objects.get(pk=1)
        self.voided_by = voided_by
        self.save()
    
    def undelete(self, *args, **kwargs):
        if self.voided:
            self.voided = False
            self.date_voided = None
            self.void_reason = None
            self.voided_by = None
            self.save()
    
    def purge(self, *args, **kwargs):
        self.delete()


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

    def update(self, updated_by=None, *args, **kwargs):
        self.date_updated = timezone.now()
        if (not updated_by):
            updated_by = User.objects.get(pk=1)
        self.updated_by = updated_by
        self.save()
    
    def delete(self, voided_by=None, *args, **kwargs):
        self.voided = True
        self.date_voided = timezone.now()
        if (not self.void_reason):
            self.void_reason = 'Voided without providing a reason'
        if (not voided_by):
            voided_by = User.objects.get(pk=1)
        self.voided_by = voided_by
        self.save()
    
    def undelete(self, *args, **kwargs):
        if self.voided:
            self.voided = False
            self.date_voided = None
            self.void_reason = None
            self.voided_by = None
            self.save()
    
    def purge(self, *args, **kwargs):
        self.delete()


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

    def update(self, updated_by=None, *args, **kwargs):
        self.date_updated = timezone.now()
        if (not updated_by):
            updated_by = User.objects.get(pk=1)
        self.updated_by = updated_by
        self.save()
    
    def delete(self, voided_by=None, *args, **kwargs):
        self.voided = True
        self.date_voided = timezone.now()
        if (not self.void_reason):
            self.void_reason = 'Voided without providing a reason'
        if (not voided_by):
            voided_by = User.objects.get(pk=1)
        self.voided_by = voided_by
        self.save()
    
    def undelete(self, *args, **kwargs):
        if self.voided:
            self.voided = False
            self.date_voided = None
            self.void_reason = None
            self.voided_by = None
            self.save()
    
    def purge(self, *args, **kwargs):
        self.delete()


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

    def update(self, updated_by=None, *args, **kwargs):
        self.date_updated = timezone.now()
        if (not updated_by):
            updated_by = User.objects.get(pk=1)
        self.updated_by = updated_by
        self.save()
    
    def delete(self, voided_by=None, *args, **kwargs):
        self.voided = True
        self.date_voided = timezone.now()
        if (not self.void_reason):
            self.void_reason = 'Voided without providing a reason'
        if (not voided_by):
            voided_by = User.objects.get(pk=1)
        self.voided_by = voided_by
        self.save()
    
    def undelete(self, *args, **kwargs):
        if self.voided:
            self.voided = False
            self.date_voided = None
            self.void_reason = None
            self.voided_by = None
            self.save()
    
    def purge(self, *args, **kwargs):
        self.delete()





    
