from django.contrib import admin
from .models import Profile, MedicalInfo


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = "user", "occupation", "telephone", "address", "is_doctor"
    list_filter = "is_doctor", "occupation"
    readonly_fields = "user",


@admin.register(MedicalInfo)
class MedicalInfoAdmin(admin.ModelAdmin):
    '''Admin View for MedicalInfo'''

    list_display = ('patient',)
    list_filter = ('surgery', 'illness', 'medication', 'nervous_disorders')
    search_fields = ('patient',)
