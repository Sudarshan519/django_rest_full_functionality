from rest_framework.decorators import api_view, schema
from django.shortcuts import get_list_or_404, render 
from django.http import HttpResponse,JsonResponse
from django.views.generic import CreateView
from hajir.decorators import IsEmployee, IsEmployer, employee_required
from users.models import CustomUser
from drf_yasg.utils import swagger_auto_schema

from users.serializers import VerifyOtpSerializer 
from .serializers import *
from rest_framework.parsers import JSONParser
import pyotp
import datetime
import base64
from rest_framework_simplejwt.tokens import RefreshToken

from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.cache import cache_page
# OTP HELPERS
class generateKey:
    @staticmethod
    def returnValue(phone): 
        return str(phone) + str(datetime.datetime.now().day) + "Some Random Secret Key"

def otp_from_phone(phone):
    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
    return pyotp.HOTP(key) 
def verifyotp(phone,otp,counter):
    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
    OTP = pyotp.HOTP(key)
    return OTP.verify(otp,counter)


#  TOKEH HELPER FUNCTION
def fetchToken(user):
        refresh = RefreshToken.for_user(user) 
        return  ({ 
            "access_token":str(refresh.access_token),
            "refresh_token":str(refresh),
        })
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@swagger_auto_schema(tags=['login'],method='post', operation_description='',request_body=PhoneSerializer)
@api_view(['POST'])
def login(request):
    try: 
        print(request.data)
        phone=request.data['phone']
        user, created =CustomUser.objects.get_or_create(email=str(phone))
        user.counter+=1
        user.is_employee=True
        user.is_employer=False
        user.wallet_user=False
        user.save()
        OTP=otp_from_phone(phone)
        try:
            return JsonResponse({"status":True,"data":OTP.at(user.counter)})
        except Exception as e:
            
            return JsonResponse({"status":True,"data":str(e)+"Failed"})
    except Exception as e:
        print(e)
        return JsonResponse({"status":True,"data":str(e)})
    

@swagger_auto_schema(tags=['login'],method='post', operation_description='',request_body=VerifyOtpSerializer)
@api_view(['POST'])
def verify_phone(request):
    phone=request.data['phone']
    otp=request.data['otp']
    try:
        user=CustomUser.objects.get(email=str(phone))
        print(user)
        if not user:
            return JsonResponse({})
        else:
            counter=user.counter
            isvalid=verifyotp(phone,otp,counter)
            if isvalid:
                try:
                    tokens=fetchToken(user)
                    return JsonResponse(tokens)
                except Exception as e:
                    return JsonResponse({"error":str(e)+"Something went wrong"})
            return JsonResponse({"status":True,"data":"Otp verified"})
    except Exception as e:
        return JsonResponse({"status":True,"data":str(e)+"Otp is wrong/invalid"})

# from .models import Employee
# from .forms import EmployeeSignupForm
# Create your views here.
@api_view(['GET'])
def get_ip_address(request):
    """ use requestobject to fetch client machine's IP Address """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')    ### Real IP address of client Machine
    
    return JsonResponse({"id":ip})
    return HttpResponse(ip)  


# class EmployeeCreateView(CreateView):
#     model = Employee
#     form_class=EmployeeSignupForm
#     template_name = "signup.html"

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'employee'
#         return super().get_context_data(**kwargs)
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
@api_view(['GET'])
# @login_required
# @employee_required 
@permission_classes([permissions.IsAuthenticated,IsEmployer])
def employee_dashboard(request):
    return Response({"status":True})


class EmployeeDashboard(APIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = [permissions.IsAuthenticated,IsEmployee]
    # @permission_classes([permissions.IsAuthenticated])
    # @login_required
    # @employee_required
    def get(self, request, format=None):
        employee=Employee.objects.get(employee_user=request.user)
        # all_invitations=Invitations.objects.all()
        active_invitations=Invitations.objects.filter(employee=employee,accepted=False)
        inactive_invitations=Invitations.objects.filter(employee=employee,accepted=True)
        
        print(inactive_invitations)
        company_list=Company.objects.all()
        serializer=InvitationSerializer(active_invitations,many=True)
        active_companies=InvitationSerializer(inactive_invitations,many=True)
        return Response({"status":True,"inactive":serializer.data,"active":active_companies.data})
class AcceptInvitation(APIView):
    @staticmethod
    @swagger_auto_schema(tags=['accept-invitation'], operation_description='accept invitation',request_body=AcceptInvitationSerializer)
    def post(request,format=None): 
        serializer=AcceptInvitationSerializer(data=request.data)
        employee=Employee.objects.get(employee_user=request.user)
        if serializer.is_valid():
            print(True)
        else:
            return Response( serializer.errors)
        try:
            id=request.data['id']
            invitation=Invitations.objects.get(id=id)
             
            invitation.accepted=request.data['accept']
            invitation.save()
            # data=get_list_or_404(companyInvitation)
        except:
            return Response({"error":"Invalid Invitation"},status=404)
        return Response({})
    

class EmployerDashboard(APIView):
    permission_classes = [permissions.IsAuthenticated,IsEmployer]
    @cache_page(60 * 15)
    @vary_on_cookie
    def get(self,request,format=None):
        return Response({"status":True})

from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle

class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'

@api_view(['GET'])
@throttle_classes([OncePerDayUserThrottle])
def view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})

def print_cache():
    sum=0
    for i in range(100000):
        sum=sum+i
    return sum

@api_view(['GET'])
@cache_page(60 * 60*24)
@vary_on_cookie
@permission_classes([permissions.IsAuthenticated,IsEmployee])
def get_weekly_report(request):
    print_cache()
    attendance=Attendance.objects.filter(login_date__gte=datetime.datetime.now()-datetime.timedelta(days=7),employee=request.user)#.filter(login_date__gte=datetime.now()-datetime.timedelta(days=7))
    serializer=AttendanceSerializer(attendance,many=True)

    return Response(serializer.data)

