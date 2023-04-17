from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class ResidenceType(models.Model):
    name=models.CharField(blank=True,max_length=255)
    def __str__(self):
        return self.name
        
class StatusOfResidence(models.Model):
    name = models.CharField(max_length=255)
    residence_type = models.ForeignKey(ResidenceType ,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Profession(models.Model):
    name_en= models.CharField(blank=True,max_length=255)
    # residence_type = models.ForeignKey(ResidenceType ,on_delete=models.CASCADE,default=0,null=True,blank=True)
    status_of_residence=models.ForeignKey(StatusOfResidence,on_delete=models.CASCADE,default=0,null=True,blank=True)
    def __str__(self):
        return self.name_en
    def statusOfResidenceEn(self):
        return self.status_of_residence.name
    def residenceType(self):
        return self.status_of_residence.residence_type.name
class UserDocuments(models.Model):
    user=models.ForeignKey("users.CustomUser", verbose_name=_("User"), on_delete=models.CASCADE)
    password_image=models.FileField(_("Passport Images"), upload_to=None, max_length=100,null=True,blank=True)
    def __str__(self):
        return self.user
    
class Profile(models.Model):
    user=models.ForeignKey("users.CustomUser",default=1, verbose_name=_("User"), on_delete=models.CASCADE)
    profile_type= models.ForeignKey(ResidenceType,default=1, on_delete=models.CASCADE)
    first_name = models.CharField(blank = True, max_length = 20)                      
    last_name = models.CharField(blank = True, max_length = 20) 
    title=models.IntegerField(choices=((1,"Mr"),(2,"Mrs")),default=1)
    country_of_residence=models.CharField(_("Country of residence"),default="Japan", max_length=50)
    status_of_residence=models.CharField(_("Status of residence"),default="Skilled Professional",max_length=100)
    profession=models.CharField(_("Profession"),default='', max_length=50)
    passport_number=models.CharField(_("Passport Number"),default='1234', max_length=50)
    documents= models.ForeignKey(UserDocuments, verbose_name=_("documents"),null=True, on_delete=models.CASCADE)
    password_front=models.FileField(_("Passport Front"), upload_to=None, max_length=100,null=True,blank=True)
    password_back=models.FileField(_("Passport Back"), upload_to=None, max_length=100,null=True,blank=True)
    organization_type=models.CharField(_("Organization Type"), max_length=100,default='None')
    business_name=models.CharField(_("Business Name"), max_length=50,default="None")
    registration_number=models.CharField(_("Registration number"), max_length=50,blank=True,null=True)
    def __str__(self):
        return self.user

class ProfileDocuments(models.Model):
    
    user=models.ForeignKey("users.CustomUser",default=1,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=False )
    front_img=models.ImageField(_("Front Image"), upload_to='media/', height_field=None, width_field=None, max_length=None,null=False,blank=False)
    back_img=models.ImageField(_("Back Image"), upload_to='media', height_field=None, width_field=None, max_length=None,)
    tilted=models.ImageField(_("Tilted Image"), upload_to='media', height_field=None, width_field=None, max_length=None,)
    selfie=models.ImageField(_("Selfie Image"), upload_to='media', height_field=None, width_field=None, max_length=None,)
    blink=models.ImageField(_("Blink Image"), upload_to='media', height_field=None, width_field=None, max_length=None,)
    def __str__(self) -> str:
        return self.user.email


    def front_img_preview(self): #new
        return mark_safe('<img src = "{url}" height = "80" width="80"/>'.format(
             url = self.front_img.url
         ))

    def back_img_preview(self): #new
        return mark_safe('<img src = "{url}" height = "80" width="80"/>'.format(
             url = self.back_img.url
         ))

    def tilted_preview(self): #new
        return mark_safe('<img src = "{url}" height = "80" width="80"/>'.format(
             url = self.tilted.url
         ))
        
    def profile_preview(self): #new
        return mark_safe('<img src = "{url}" height = "80" width="80"/>'.format(
             url = self.tilted.url
         ))
    def blink_preview(self):
        return mark_safe('<img src = "{url}" height = "80" width="80"/>'.format(
             url = self.blink.url
         ))
    class Meta:
        ordering=('-created_at',)

    def __str__(self):
        return self.user
    
class TermsAndConditions(models.Model):
    name=models.CharField(_("Type"), max_length=50)
    detail=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name
    

class IntendedUseOfAccount(models.Model):
    name=models.CharField(_("Indended Use of Account"), max_length=50)
    def __str__(self):
        return self.name
    
class Ekyc(models.Model):   
    user=models.ForeignKey("users.CustomUser",default=1, verbose_name=_("User"), on_delete=models.CASCADE)
    front_img=models.ImageField(_("Front Image"), upload_to='media/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    back_img=models.ImageField(_("Back Image"), upload_to='media', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    tilted=models.ImageField(_("Tilted Image"), upload_to='media', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    indended_use_of_account=models.CharField(_("Indended Use of Account"), max_length=50,default="own_use")
    mobile_number=models.CharField(_("Mobile Number"), max_length=50)
    phone_number=models.CharField(_("Phone Number"),max_length=20)
    gender=models.CharField(_("Gender"), max_length=50)
    date_of_issue=models.DateField(_("Date of issue"), auto_now=False, auto_now_add=False)
    peroid_of_stay=models.DateField(_("Peroid of stay"), auto_now=False, auto_now_add=False)
    expiry_date=models.DateField(_("Expiry Date"), auto_now=False, auto_now_add=False)  
    postal=models.CharField(_("Postal Code"), max_length=50)
    prefature=models.CharField(_("Prefecture"), max_length=50)
    city=models.CharField(_("City"), max_length=50)
    building_name_or_number=models.CharField(_("Building Name/ Number"), max_length=50)
    nationality=models.CharField(_("Nationality"), max_length=50)
    source_of_income=models.FileField(_("Source of Income"), upload_to='media', max_length=100,null=True,blank=True)
    tax_return=models.FileField(_("Tax Return"), upload_to='media', max_length=100,null=True,blank=True)
    audit_report=models.FileField(_("Audit Report"), upload_to='media', max_length=100,null=True,blank=True)
    created_at=models.DateTimeField(_(""), auto_now=True,  )
    def __str__(self):
        return self.user



# class UserLimit(models.Model):

class CustomUser(AbstractBaseUser, PermissionsMixin):
    is_employee=models.BooleanField(_("Employee"),default=False)
    is_employer=models.BooleanField(_("Employer"),default=False)
    wallet_user=models.BooleanField(_("Wallet User"),default=True)
    CHOICES=((1,"Japanese"),(2,"Foreigner"))
    is_employee=models.BooleanField(_("IsEmployee"),default=True)
    is_employer=models.BooleanField(_("IsEmployer"),default=False)
    email = models.EmailField(_("email address"),default="no@mail.com", unique=True,null=False,)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now) 
    resident_type=models.IntegerField(choices=CHOICES ,default=1)
    is_business_user=models.BooleanField(default=False)
    emailVerified=models.BooleanField(blank=False,default=False)
    profileVerified=models.BooleanField(blank=False,default=False)
    kycVerified=models.IntegerField(
        choices=((0,'Uniniialized'),(1,'Pending'),(2,'Verified'),),
        blank=False,default=0)
    kyc_type=models.ForeignKey("users.EKycType", on_delete=models.CASCADE,blank=True,null=True)
    gps=models.CharField(max_length=60,default="")
    counter = models.IntegerField(default=0, blank=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


    def kyc_updated(self):
        data=self.ekyc_set.all()
        return True if len(data)>0 else False

    def profile_updated(self):
        data=self.profile_set.all()
        if len(data)>0:
            return True
        else:
            return False

    # def check_limit(self):
    #     print(self.kyc_type)
    #     # TODO CHECK DAILY LIMIT
    #     return True
    # def check_daily_limit(self):
    #     # TODO CHECK DAILY LIMIT
    #     return True
    # def check_monthly_limit(self):
    #     # TODO CHECK DAILY LIMIT
    #     return True
    # def check_quaterly_limit(self):
    #     # TODO CHECK DAILY LIMIT
    #     return True
    # def check_yearly_limit(self):
    #     # TODO CHECK DAILY LIMIT
    #     return True

    def all_users(self):
        self.objects.all()

    # @property
    # def is_staff(self):
    #     # Handle whether the user is a member of staff?"
    #     return self.is_admin
# class phoneModel(models.Model):
#     Mobile = models.IntegerField(blank=False)
#     isVerified = models.BooleanField(blank=False, default=False)
#     counter = models.IntegerField(default=0, blank=False)
#     def __str__(self):
#         return str(self.Mobile)
# type_choices=((0,'Android'),(1,'Ios'))
# class AppVersion(models.Model):
#     action_choices=((1,'Soft Update'),(2,'Force Update'),(3,'Maintainence'))
#     type=models.IntegerField(choices=type_choices,default=0)
#     title=models.CharField(max_length=20,default='')
#     version=models.CharField(max_length=20,default='')
#     message=models.CharField(max_length=255,default='')
#     update_action=models.IntegerField(choices=action_choices,default=1)
    
# class AndroidVersion(BaseVersion):
#     type=models.IntegerField(default=0)
#     created_at=models.DateTimeField(auto_now=True)  
# class IosVersion(BaseVersion):
#     type=models.IntegerField(default=1)
#     created_at=models.DateTimeField(auto_now=True)  
from django.utils.html import mark_safe
class Banners(models.Model):
    title=models.CharField(max_length=255,null=True,blank=True)
    redirect_url=models.CharField(max_length=255,null=True,blank=True)
    image=models.ImageField(upload_to='media',default='info.png')
    active=models.BooleanField(default=True)
    # def __str__(self) -> str:
    #     return "<img src={self.image}"
    def img_preview(self): #new
        return mark_safe('<img src = "{url}" height = "80" width="80"/>'.format(
             url = self.image.url
         ))

class PostalCode(models.Model):
    country=models.CharField(max_length=100,default="Nepal")
    district=models.CharField(max_length=255,default='')
    post_office=models.CharField(_("Post office"), max_length=50)
    postal_pin_code=models.CharField(_("Postal/Pin Code"), max_length=100)
    postal_office_type=models.CharField(_("Post Office Type"), max_length=50)
    # def __str__(self):
    #     return self.district

class CurrencyRate(models.Model):
    created_at=models.DateTimeField(_("Created Date"), auto_now=False, auto_now_add=True,null=True)
    updated_at=models.DateTimeField(_("Updated Date"), auto_now=True, auto_now_add=False,null=True)
    iso3=models.CharField(_("ISO3"), max_length=50)
    name=models.CharField(_("NAME"), max_length=50)
    unit=models.IntegerField(_("Unit"),default=1)
    buy=models.FloatField(_("Buy"))
    sell=models.FloatField(_("Sell"))
    # def __str__(self):
    #     return f'{self.name} {self.created_at} {self.updated_at} {self.name} {self.buy} {self.sell}'
    
    
class ProvinceDistricts(models.Model):
    country=models.CharField(max_length=100,default="Nepal")
    district=models.CharField(max_length=255,default='')
    province=models.CharField(max_length=255,default='')
    def __str__(self):
        return self.province + " "+ self.district
    
class Country(models.Model):
    country=models.CharField(_("Country"), max_length=150)
    continent=models.CharField(_("Continent"), max_length=50)
    estimate=models.CharField(_("Estimate"), max_length=50)
    year=models.CharField(_("Year"), max_length=50)
    estimate2=models.CharField(_("Estimate2"), max_length=50)
    year2=models.CharField(_("Year2"), max_length=50)
    flag_img=models.URLField(_("flag image"), max_length=200)

    def img_preview(self): #new
        return mark_safe('<img src = "{url}" height = "80" width="80"/>'.format(
             url = "https:"+self.flag_img
         ))


from django.conf import settings
class TransactionType(models.Model):
    CHOICES=((0,"Credit Card"),(2,"Bank"),(3,"Cash"),(4,"Wallet"))
    transaction_type=models.IntegerField(_("Transactions type"),choices=CHOICES)
    name=models.CharField(_("name"), max_length=50)
    account_number=models.IntegerField(_("Account Number"))
    # account_holder_name=models.CharField(_("Account Name"), max_length=150)
from django.core.validators import MaxValueValidator, MinValueValidator
class Transactions(models.Model):
    created_at=models.DateTimeField(_("Created Date"),auto_now_add=True)
    updated_at=models.DateTimeField(_("Updated Date"),auto_now=True)
    amount=models.FloatField(_("Transaction Amount"),validators=[MinValueValidator(10.0),],)
    transaction_by=models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE,related_name="users_send")
    transaction_to=models.ForeignKey("users.CustomUser",  on_delete=models.CASCADE,related_name="users_received")
    charge_amount=models.FloatField(_("Charge Amount"),default=50.0)
    transaction_type=models.ForeignKey("users.TransactionType",   on_delete=models.CASCADE)
    remarks=models.CharField(_("Remarks"), max_length=150)


class EkycType(models.Model):
    CHOICES=((1,"Unverified"),(2,"Basic"),(3,"Full"))
    status=models.IntegerField(_("EKYC Type"),choices=CHOICES ,default=0)
    transactions_limit_per_day=models.IntegerField(_("Transactions limit per day"))
    transactions_limit_per_month=models.IntegerField(_("Transactions limit by month"))
    transactions_limit_per_six_months=models.IntegerField(_("Transactions limit by half year"))
    transactions_limit_per_year=models.IntegerField(_("Transactions limit by year"))
    transactions_amount_per_day=models.IntegerField(_("Transactions amount per day"))
    transactions_amount_per_month=models.IntegerField(_("Transactions amount by month"))
    transactions_amount_per_six_months=models.IntegerField(_("Transactions amount by half year"))
    transactions_amount_per_year=models.IntegerField(_("Transactions amount by year"))
    def __str__(self):
        return self.CHOICES[self.status-1][1]
    
    def isFullKyc(slef):
        return self.status==3
    
    def isBasicKyc(self):
        return self.status==2

    def isAuthorized(self):
        return self.status != 0