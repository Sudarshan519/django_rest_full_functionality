from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# class User(AbstractUser):
    # is_employee=models.BooleanField(_("Employee"),default=False)
    # is_employer=models.BooleanField(_("Employer"),default=False)
    # wallet_user=models.BooleanField(_("Wallet User"),default=False)
 
# # class EmployerUser(models.Model):
# #     user=models.OneToOneField(User, verbose_name=_("Employer User"), on_delete=models.CASCADE)

# # class EmployeeUser(models.Model):
# #     user=models.OneToOneField(User, verbose_name=_("Employee User"), on_delete=models.CASCADE)
# class HajirUser(CustomUser):
#     staff_code=models.CharField(_("Staff Code"), max_length=50)
    
class BusinessLeaveDays(models.Model):
    class Days(models.TextChoices):
        sunday='sun',_("Sunday")
        monday='mon',_("Monday")
        tuesday='tue',_("Tuesday")
        wednesday='wed',_("Wednesday")
        thursday='thu',_("Thursday")
        friday='fri',_("Friday")
        saturday='sat',_("Saturday")
    # company_name=models.ForeignKey("hajir.Company",  related_name="business",null=True, on_delete=models.CASCADE)
    day=models.CharField(_("Day"),choices=Days.choices,default=1, max_length=50)
    def __str__(self):
        return self.day
    
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
# # Create your models here.
# from django.utils import timezone
# timedelta=timezone.now
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
    # business_leave_days=models.ManyToManyField("hajir.BusinessLeaveDays", )
    # special_leave_days=models.ForeignKey("hajir.SpecialLeaveDays", verbose_name=_("special leave"), on_delete=models.CASCADE)
    office_hour_start=models.TimeField(_("Office hour start"), auto_now=False, auto_now_add=False)
    #models.CharField(_("Office hour start"), max_length=50)
    office_hour_end =models.TimeField(_("Office hour end"), )
    access_network=models.CharField(_("Access Network"), max_length=50)
    probablation_peroid=models.CharField(_("Probablation Peroid"),choices=(('1',"1 months"),('3',"3 Months"),('6',"6 Months")),default=3, max_length=50)
    # sick_leave=models.ForeignKey("hajir.SickLeave", verbose_name=_("sick leave"),null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Employee(CustomUser):
    employee_id=models.AutoField(_("employee id"),primary_key=True)
    company=models.ManyToManyField("hajir.Company", verbose_name=_("Company List"))#models.ForeignKey("hajir.Company", verbose_name=_("EmployeCompany"), on_delete=models.CASCADE,null=True)
    fullname=models.CharField(_("Full Name"), max_length=50)
    designation=models.CharField(_("Designation"), max_length=50)
    mobilenumber=models.IntegerField(_("Mobile number"))
    # email=models.EmailField(_("Email"), max_length=254)
    dateofbirth=models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False)
    salary_type=models.CharField(_("Salary Type"),choices=(('calendar','Calendar Days'),('30day','30 Days')), max_length=50)
    salary_amount=models.IntegerField(_("Salary Amount"),default=1400)   
    joining_date=models.DateField(_("Joining Date"), auto_now=False, auto_now_add=False,)
    duty_time=models.TimeField(_("Duty Time"), auto_now=False, auto_now_add=False,)
    working_hours=models.DurationField(_("Working Hours"),)  
    overtime_ratio=models.IntegerField(_("Overtime Ratio"),default=0)
    allowlateby=models.DurationField(_("Allow late by"),)
    allowance=models.FloatField(_("Allowance"),null=True,blank=True)
    casual_leave=models.IntegerField(_("Casual Leave Days"),default=0)
    staffcode=models.CharField(_("Staff Code"), max_length=50,blank=True,null=True)


class Attendance(models.Model):
    login_date=models.DateTimeField(_("Login Date"), auto_now=False, auto_now_add=True)
    login_time=models.TimeField(_("Login Time"), auto_now=False, auto_now_add=False )
    logout_time=models.TimeField(_("Logout Time"), auto_now=False, auto_now_add=False,)
    break_start_time=models.TimeField(_("Break Start Time"), auto_now=False, auto_now_add=False,)
    break_end_time=models.TimeField(_("Break End Time"), auto_now=False, auto_now_add=False,)