 
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
# admin.site.register(PostalCode)
@admin.register(PostalCode)
class PostalCodeAdmin(admin.ModelAdmin):
    list_display=[k.name  for k in PostalCode._meta.fields]
# admin.site.register(CurrencyRate)
# @admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    # list_display=["name","created_at","updated_at"]
    list_display=[k.name  for k in CurrencyRate._meta.fields]
    # list_display=[k for k in CurrencyRate._meta.get_fields()]
    # list_dispaly=('sell')#(k for k in CurrencyRate._meta.get_fields())
    list_filter = ('name','buy','sell', 'created_at','updated_at',)
    # list_display=['name','buy','sell', 'created_at','updated_at',]
    search_fields = ("name",'iso3')
admin.site.register(CurrencyRate,CurrencyRateAdmin)
# admin.site.register(ProfileDocuments)
@admin.register(ProfileDocuments)
class ProfileDocumentsAdmin(admin.ModelAdmin):
    # date_hierarchy = 'pub_date'
    list_display = ['id','user', 'created_at','updated_at','front_img_preview','back_img_preview','tilted_preview','blink_preview']

admin.site.register(ProvinceDistricts)

class BannersAdmin(admin.ModelAdmin): # new
    readonly_fields = ['img_preview']
    list_display = ['title', 'img_preview']
admin.site.register(Banners,BannersAdmin)
admin.site.site_header='Clone RPS Remit'

class CountryAdmin(admin.ModelAdmin):
    list_display=["img_preview","country","continent"]

admin.site.register(Country,CountryAdmin)