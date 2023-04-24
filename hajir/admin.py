from django.contrib import admin
from .models import *
# Register your models here. 
admin.site.register(Company)
admin.site.register(BusinessLeaveDays)
admin.site.register(GovernmentLeaveDays)
admin.site.register(SpecialLeaveDays)
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Invitations)
admin.site.register(LeaveDays)