 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email","resident_type","emailVerified", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ResidenceType)
admin.site.register(StatusOfResidence)
admin.site.register(Profession)
admin.site.register(Profile)
admin.site.register(UserDocuments)
admin.site.register(TermsAndConditions)
admin.site.register(IntendedUseOfAccount)
admin.site.register(Ekyc) 
admin.site.register(AppVersion)
 
admin.site.register(ProfileDocuments)
class BannersAdmin(admin.ModelAdmin): # new
    readonly_fields = ['img_preview']
    list_display = ['title', 'img_preview']
# admin.site.register(Banners,BannersAdmin)
admin.site.site_header='Clone RPS Remit'
