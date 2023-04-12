from django.db import models
from django.utils.translation import gettext_lazy as _


class BusinessLeaveDays(models.Model):
    class Days(models.TextChoices):
        sunday='sun',_("Sunday")
        monday='mon',_("Monday")
        tuesday='tue',_("Tuesday")
        wednesday='wed',_("Wednesday")
        thursday='thu',_("Thursday")
        friday='fri',_("Friday")
        saturday='sat',_("Saturday")
    company_name=models.ForeignKey("hajir.Company",  related_name="business",null=True, on_delete=models.CASCADE)
    day=models.CharField(_("Day"),choices=Days.choices,default=1, max_length=50)
class SpecialLeaveDays(models.Model):
    name=models.CharField(_("Leave Name"), max_length=50)
    leave_date=models.DateField(_("Leave Date"), auto_now=False, auto_now_add=False)
    company_name=models.ForeignKey("hajir.Company",  related_name="company",null=True, on_delete=models.CASCADE)
class GovernmentLeaveDays(models.Model):
    name=models.CharField(_("Leave Name"), max_length=50)
    leave_date=models.DateField(_("Leave Date"), auto_now=False, auto_now_add=False)
    company_name=models.ForeignKey("hajir.Company", related_name='gov',null=True, on_delete=models.CASCADE)
class SickLeave(models.Model):
    CHOICES=(('m','Monthly'),('w','Weekly'),('y','Yearly'))
    total_days=models.IntegerField(_("Total Leave Days"))
    leave_by=models.CharField(_("Leave By"),choices=CHOICES,default='m', max_length=50)
    # company_name=models.ForeignKey("hajir.Company", related_name='gov',null=True, on_delete=models.CASCADE)
# Create your models here.
class Company(models.Model):
    class StaffCode(models.TextChoices):
        auto='AUTO',_('Auto')
        custom='Custom',_('Custom')
    name=models.CharField(_("Company Name"), max_length=100)
    phone=models.IntegerField(_("Phone"))
    address=models.CharField(_("Address"), max_length=50)
    staffcode=models.CharField(_("Staff Code Type"),
    choices=StaffCode.choices,max_length=50,default=StaffCode.auto,)
    
    #   sunday =1 and so on
    # business_leave_days=models.ForeignKey(BusinessLeaveDays,  on_delete=models.CASCADE)
    # special_leave_days=models.ForeignKey("hajir.SpecialLeaveDays", verbose_name=_("special leave"), on_delete=models.CASCADE)
    office_hour_start=models.CharField(_("Office hour start"), max_length=50)
    office_hour_end =models.CharField(_("Office hour end"), max_length=50)
    access_network=models.CharField(_("Access Network"), max_length=50)
    probablation_peroid=models.CharField(_("Probablation Peroid"),choices=((1,"1 months"),(3,"3 Months"),(6,"6 Months")),default=3, max_length=50)
    # sick_leave=models.ForeignKey("hajir.SickLeave", verbose_name=_("sick leave"),null=True, on_delete=models.CASCADE)
