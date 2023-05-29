from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from CharityGo.models import NGO, Campaign

from django.utils import timezone

# Register your models here.
@admin.register(NGO)
class NGOAdmin(admin.ModelAdmin):
    fields = ["user", "ngo_name", "ngo_address", "ngo_description", "ngo_phone", "ngo_image", "ngo_bank_name", "ngo_account_title", "ngo_account_no"]
    list_filter = ("ngo_name",)

    def has_delete_permission(self, request, obj=None):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True
    
    def save_model(self, request, obj, form, change):
        # Set the created_by field to the current user during record creation
        if not change:
            obj.created_by = request.user
            obj.date_created = timezone.now()

        super().save_model(request, obj, form, change)
    
@admin.register(Campaign)
class NGOAdmin(admin.ModelAdmin):

    fields = ["campaign_name", "campaign_description", "campaign_image", "NGO"]    
    #list_display = ("campaign_name", "campaign_description", "campaign_image", "created_by",)
    #readonly_fields = ("created_by", "date_created",)
    # exclude = ("date_updated", "updated_by", "voided", "date_voided", "voided_by", "void_reason")

    def has_delete_permission(self, request, obj=None):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True
    
    def save_model(self, request, obj, form, change):
        # Set the created_by field to the current user during record creation
        if not change:
            obj.created_by = request.user
            obj.date_created = timezone.now()

        super().save_model(request, obj, form, change)
    