import datetime

from django.shortcuts import get_list_or_404, get_object_or_404

from users.postal_code import getAddress
# from django import views
# from django.contrib.auth.models import User, Group
# from rest_framework.parsers import JSONParser
from .models import CustomUser
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action
from rest_framework.views import APIView
import pyotp
import base64
from drf_yasg.utils import swagger_auto_schema 
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.cache import cache_page


from django.shortcuts import render

def chat_box(request, chat_box_name):
    # we will get the chatbox name from the url
    return render(request, "chatbox.html", {"chat_box_name": chat_box_name})
# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(phone): 
        return str(phone) + str(datetime.datetime.now().day) + "Some Random Secret Key"

def otp_from_email(email):
    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(email).encode())  # Key is generated
    return pyotp.HOTP(key) 
def verifyotp(otp,counter):
    keygen = generateKey()
    key = base64.b32encode(keygen.returnValue(email).encode())  # Key is generated
    OTP = pyotp.HOTP(key)
    return OTP.verify(otp,counter)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

@swagger_auto_schema(tags=['user'],method='post', operation_description='',request_body=RegisterSerializer)
@api_view(['POST'])

def register(request):
    serializer=RegisterSerializer(data=request.data)
    
    if serializer.is_valid():
        user=serializer.save()
        OTP=otp_from_email(serializer.data['email'])
        # request.headers['email']=serializer.data['email']
        # getPhoneNumberRegistered.get(request),#,email=serializer.data['email'])
        return Response({"otp":OTP.at(user.counter)},status=status.HTTP_201_CREATED)
        getPhoneNumberRegistered.get(email=serializer.data['email'])
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def get_access_token(request):
    return 
from django.forms.models import model_to_dict
def fetchToken(user):
    try:
        refresh = RefreshToken.for_user(user)
    
        return  ({
            # "user":user.__dict__,
            # "cuser":model_to_dict(user),
            # "model":model_to_dict(user),
            "email":user.email,
            "ekyc_verified":user.kyc_updated(),
            "isEmailVerified":user.emailVerified,
            "access_token":str(refresh.access_token),
            "refresh_token":str(refresh),
            # "profile_updated":user.profile_updated
        })
    except Exception as e :
        return  str(e)
 
class LoginView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema(tags=['user'], operation_description='otp',request_body=LoginSerializer)
    def post(self, request, refreshformat=None):
        serializer = LoginSerializer(data=request.data,
            context={ 'request': request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        try:
            if(user.emailVerified):
                data=fetchToken(user) 
                return Response(data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"error":"email not verified"})
        except Exception as e:
            print('test')
        
 
        return Response(data, status=status.HTTP_202_ACCEPTED)
# @api_view(['POST'])
# def login(request):
#     # email=request.data['email']
#     # password=request.data['password']
#     # user=authenticate(username=email,password=password)
#     # print(user)
#     # if user is not None:
#     #     email=user.email
#     #     token=Token.objects.get_or_create(user_id=user.id)
#     #     print(token)
#     #     return Response({
#     #     "status":True,
#     #     "email":email,
#     #     "data":{
#     #         "access_token":token
#     #     }
#     # })
    
#     try:
#         serializers=LoginSerializers(data=request.data)

#     # getPhoneNumberRegistered.get(email=request.data['email'])
#         return Response({
#             "status":True,
#             "data":{
#                 "access_token"
#             }
#         })
#     except:
#         return Response(serializers.errors)
# from drf_yasg import openapi
# header_param = openapi.Parameter('email',openapi.IN_QUERY,description="local header param", type=openapi.IN_BODY)


@api_view(['GET'])
def get_otp(request,email):#email
 
        try:
            user = CustomUser.objects.get(email=email)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            return Response({"error":"User not registered"},404)
        OTP=otp_from_email(email)
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return  Response({"OTP": OTP.at(user.counter)})  # Just for demonstration
@api_view(['POST'])
@swagger_auto_schema(tags=['user'], operation_description='otp',request_body=VerifyOtpSerializer)
def verify_otp(request):
    email=request.data['email']
    otp=request.data['otp']
    try:
        user=CustomUser.objects.get(email__iexact=email)
        isvalid=verifyotp(otp,user.counter)
        if isvalid:
            return Response({
                "status":true,
                "data":"Email verified"
            })
        return Response({"error":"Otp invalid/expired"})
    except:
        return Response({"error":"Otp invalid/expired"})
class getPhoneNumberRegistered(APIView): 
    # @staticmethod
    # @swagger_auto_schema(tags=['user'], operation_description='' )
    # def get(request,email):#email
    #     # email=request.data['email']
    #     user=None
    #     try:
    #         user=CustomUser.objects.get(email=email)
    #         if( user is not None):
    #             print(user.email)
    #             user.counter+=1
    #             user.save()
                
    #             return JsonResponse({'data':OTP.at(user.counter)})
         
    #     except ObjectDoesNotExist:
    #         user=CustomUser.objects.create(email=email)
    #             # user.counter+=1
    #         user.save()
            
    #         return JsonResponse({'data':OTP.at(user.counter)}) 
    #     except Exception as e:
    #         print(e)
 


    #     keygen = generateKey()
    #     key = base64.b32encode(keygen.returnValue(user.email).encode())  # Key is generated
    #     OTP = pyotp.HOTP(key)
    #     print(OTP.verify('576486',30))
    #     otp=OTP.at(1234)
    #     newotp=OTP.at(user.counter)
    #     print(newotp)
    #     return JsonResponse({'data':newotp,'otp':otp})
    #     phone=request.body['phone']
    #     try:
    #         user = CustomUser.objects.get(email=phone)  # if Mobile already exists the take this else create New One
    #     except ObjectDoesNotExist:
    #         # return JsonResponse({"error":"User not registered"},404)
    #         CustomUser.objects.create(
    #             email=phone,
    #         )
    #         user = CustomUser.objects.get(email=phone)  # user Newly created Model
    #     user.counter += 1  # Update Counter At every Call
    #     user.save()  # Save the data
    #     keygen = generateKey()
    #     key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
    #     OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
    #     # print(OTP.at(user.counter))
    #     # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
    #     return  JsonResponse({"OTP": OTP.at(user.counter)})  # Just for demonstration


    # This Method verifies the OTP
 
    @staticmethod
    @swagger_auto_schema(tags=['user'], operation_description='otp',request_body=VerifyOtpSerializer)
    def post(request):# email
        email=request.data['email']
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(email).encode())  # Key is generated
        OTP = pyotp.HOTP(key)

        try:
            user=CustomUser.objects.get(email__iexact=request.data["email"])
            if(OTP.verify(int(request.data['otp']),user.counter)):
                user.emailVerified=True
                user.save()
                return Response({"success":"Email Verified"})
            else:
                return JsonResponse({"error":"OTP is wrong/expired"}, status=400)
        except Exception as e:
            print(str(e))
            return JsonResponse({"error":"OTP is wrong/expired"}, status=400)
     
# class PhoneNumberOTP(APIView):
#     def get(self, request, format=None):
#         return Response({})
#     def post(self, request,format=None):
#         return Response({})
# class HelloAPi(APIView):
#     def get(self, request, pk, format=None):
#         return Response({})

def hello(request):
    return JsonResponse({"HELLOV":""},status=200)


# TODO:// FORGOT PASSWORD
# TODO:// REPORT LOGS
# TODO :// BANNER 

class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banners.objects.filter(active=True)
    serializer_class = BannerSerializer
# TODO :// EXCHANG API
# TODO :// HOME APIe
# TODO :// EKYC
# TODO :// SOCIAL LOGIN
# TODO POSTAL CODE
@api_view(['GET'])
def get_address(request,code):
    address=getAddress(code)
    return JsonResponse({"address":str(address)})


# TODO PROFILE CREATE ,UPDATE
from rest_framework import mixins

# TODO GET VERSIONS
class ProfileVersionViewSet( mixins.ListModelMixin,viewsets.GenericViewSet):
    # pass
    def list(self, request):
            queryset = ProfileDocuments.objects.filter(user=request.user)
            doc = get_list_or_404(queryset)
            serializer = ProfileDocumentsSerializer(doc,many=True,)
            return JsonResponse(serializer.data,safe=False)
    # def retrive(self, request):
    #     pass
    # def retrieve(self, request, pk=None):
    #     queryset = ProfileDocuments.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = ProfileDocumentsSerializer(user)
    #     return Response(serializer.data)
    # def create(self, request):
    #     pass
    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'retrive':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
# @api_view(['GET','POST','UPDATE'])
# def profile_documents(request):
from rest_framework.parsers import FormParser, MultiPartParser

class ProfileDocumentViewset(mixins.CreateModelMixin,viewsets.GenericViewSet):#viewsets.ModelViewSet):
    queryset = ProfileDocuments.objects.all()
    serializer_class = ProfileDocumentsSerializer
    parser_classes = (FormParser, MultiPartParser)
    pass
    """
        A simple ViewSet for listing or retrieving users.
    """
    # def list(self, request):
    #     pass
    #     queryset = ProfileDocuments.objects.all()
    #     serializer = ProfileDocumentsSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     pass
    #     queryset = ProfileDocuments.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = ProfileDocumentsSerializer(user)
    #     return Response(serializer.data)
    # def create(self, request):
    #         pass
    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
@api_view(['GET'])
def get_signup_info(request):
    residence_types=ResidenceType.objects.all()
    resident_serializer=ResidenceTypeSerializer(residence_types,many=True)
    residenceStatuss=StatusOfResidence.objects.all()
    resident_status_serializer=StatusResicenceSerializer(residenceStatuss,many=True)
    professions=Profession.objects.all()
    serializers=ProfessionSerializer(professions,many=True)
    # print(professions)
    return JsonResponse({
        "resident_types":resident_serializer.data,
        "status_of_residence":resident_status_serializer.data,
        "professions":serializers.data })
# TODO TERMS AND CONDITIONS
@api_view(['GET'])
def get_terms(requst,type=''):
    data=TermsAndConditions.objects.all()
    serializers=TermsAndConditionSerializer(data,many=True)
 
    return JsonResponse({"data": serializers.data })
    
    return JsonResponse({"error":""})
# TODO VERSION CHECK
# TODO WELCOME

# sync unit rates
# 
import json

@api_view(['GET'])
def store_postal_codes_Nepal(request):
    # PostalCode.objects.all().delete()
    data=PostalCode.objects.all()
    postal=[]
    for d in data:
        postal.append(model_to_dict(d))
    # f=open('./nepal_postal_code.json')
    # data=json.load(f)
    # postalcodes=[]
    # for i in data:
    #     postal_code=PostalCode()
    #     postal_code.district=i['district']
    #     postal_code.post_office=i['post_office']
    #     postal_code.postal_pin_code=i['postal_pin_code']
    #     postal_code.post_office_type=i['post_office_type']
    #     # postal_code.save()
    #     postal.append(postal_code)
    # PostalCode.objects.bulk_create(postal)
    # return JsonResponse({"data":data})
    return JsonResponse({"data":postal})
@cache_page(60 * 60*24)
@api_view(['GET'])
def get_disticts_provinces(request):
    f=open('./province_districts.json')
    ProvinceDistricts.objects.all().delete()
    data=json.load(f)
    provinces=[]
    for i in data:
        province_district=ProvinceDistricts()
        province_district.district=i['district']
        province_district.province=i['province']
        # print(province_district.district)
        # province_district.save()
        provinces.append(province_district)
    ProvinceDistricts.objects.bulk_create(provinces)
    return JsonResponse({"data":data})

from unicodedata import lookup

import iso3166
def flag_emoji(name):
    alpha = iso3166.countries.get(name).alpha2
    box = lambda ch: chr( ord(ch) + 0x1f1a5 )
    return box(alpha[0]) + box(alpha[1])
    print(flag_emoji("Canada"))


def print_all_flags():
    flags=""
    i=1
    data=[]

    for i, c in enumerate( iso3166.countries ):
        # print(flag_emoji(c.name), end="")
        # print(i)
        d=dict()
        d['name']=c.name
        d['flag']= (flag_emoji(c.alpha2.lower()))
        i+=1
        d['id']=i
        # print(i)
        # print(flag_emoji(c.alpha2.lower()))
        # flags=flags+c.name+"\n" +(flag_emoji(c.alpha2.lower()))+"\n"
        data.append(d)
        # return flag_emoji(c.name)
        # flags+(flag_emoji(c.name))
    return data
        # if i%25 == 24: print()
def get_emoji_flag(request):
    data=print_all_flags()
    return JsonResponse( {
        
        "allflags":print_all_flags(),
        # d['name']:d['flag'] for d in data,
        # "allflags": (print_all_flags())
        })
@api_view(['GET'])
@cache_page(60 * 60*24)
def get_country_list(request):
    f=open('./country_gdp.json')
    data=json.load(f)
    countries=[]
    for i in data:
        # print(i.get("flag_img","//upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag_of_Tuvalu.svg/23px-Flag_of_Tuvalu.svg.png"))
        country=Country()
        country.country=i['name']
        country.continent=i['continent']
        if (i.get("flag_img","//upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag_of_Tuvalu.svg/23px-Flag_of_Tuvalu.svg.png") is not None):
            country.flag_img=i.get("flag_img","//upload.wikimedia.org/wikipedia/commons/thumb/3/38/Flag_of_Tuvalu.svg/23px-Flag_of_Tuvalu.svg.png")
        country.year=i['year']
        country.estimate=i['estimate']
        country.year2=i['year_2']
        country.estimate2=i['estimate_2']
        # print(country.district)
        # country.save()
        countries.append(country)
        countries.append(country)
    Country.objects.bulk_create(countries)
    return JsonResponse({"data":data})
from .exchange_rates import get_rates
@api_view(['GET'])
def get_rates_list(request):
    data=(get_rates())
    objects=[]
    for kv in (data['data']['payload']):
        # print(kv)
        # print(data[kv])
        created_at=kv['published_on']
        # print(created_at)
        updated_at=kv['modified_on']
        for a in kv['rates']:
            # print(a)
            currencyrate=CurrencyRate()
            # currencyrate.created_at=created_at
            # currencyrate.updated_at=updated_at
            
            currencyrate.name=a['currency']['name']
            currencyrate.iso3=a['currency']['iso3']
            currencyrate.buy=a['buy']
            currencyrate.sell=a['sell']
            currencyrate.unit=a['currency']['unit']
            # print(currencyrate)
            # currencyrate.save()
            objects.append(currencyrate)

        # print(len(objects))
        CurrencyRate.objects.bulk_create(objects)
        # print(data[kv])
        # for k,v in data[kv]:
        #     print(k)
        #     print(v)

        # print(v)

    return JsonResponse({"exchange_rates":data}) #json.loads(data)})
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def home(request):
    return JsonResponse({"profile":{},"quick_send":[],"transactions":[],})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_latest_transactions(request):
    return JsonResponse({"transactions":[]},safe=True)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    return JsonResponse({"profile":[]})

# def get_model_fields(model):
#     return model._meta.fields
# def get_fields(request):
#     return get_model_fields(CurrencyRate)
    


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )


from django.db.models import F, Sum
from orders.models import  Order

from products.models import Product
from django.core import serializers
@api_view(['GET'])
def allproducts(request):
    

    # Assuming you have a specific user object (replace with the actual user)
    user = CustomUser.objects.get(email='a')

    # Annotate each product with the total_price based on the quantity ordered by the user
    product_list = Product.objects.filter(order__user=user).annotate(
        total_price=Sum(F('order__quantity') * F('price'), output_field=models.DecimalField(max_digits=10, decimal_places=2)),
    quantity_ordered=F('order__quantity'),
    order_id=F('order__id')
    ).values()

    # Iterate through the product_list and access the total_price for each product
    # for product in product_list:
    #     print(f"Product: {product.name}, Total Price for {user.email}: {product.total_price}")
    return JsonResponse({"products": list(product_list)})
    # return JsonResponse( serializers.serialize('json', product_list, fields="__all__"),safe=False)