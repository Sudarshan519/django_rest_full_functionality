from django.shortcuts import render 
from django.http import HttpResponse
from django.views.generic import CreateView
# from .models import Employee
# from .forms import EmployeeSignupForm
# Create your views here.
def get_ip_address(request):
    """ use requestobject to fetch client machine's IP Address """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')    ### Real IP address of client Machine
    return HttpResponse(ip)  


# class EmployeeCreateView(CreateView):
#     model = Employee
#     form_class=EmployeeSignupForm
#     template_name = "signup.html"

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'employee'
#         return super().get_context_data(**kwargs)
    
