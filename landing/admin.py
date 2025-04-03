from django.contrib import admin
from .models import EarlyAccessRegistration

# Register your models here.

@admin.register(EarlyAccessRegistration)
class EarlyAccessRegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'specialization', 'organization', 'want_early_access', 'registration_date')
    list_filter = ('specialization', 'want_early_access', 'registration_date')
    search_fields = ('full_name', 'email', 'phone_number', 'organization')
    readonly_fields = ('registration_date',)
