import datetime
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
# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(phone):
        # print(datetime.datetime.now())
        return str(phone) + str(datetime.datetime.now().day) + "Some Random Secret Key"




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

@swagger_auto_schema(method='post', operation_description='',request_body=RegisterSerializer)
@api_view(['POST'])

def register(request):
    print(request.data)
    serializer=RegisterSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        request.headers['email']=serializer.data['email']
        # getPhoneNumberRegistered.get(request),#,email=serializer.data['email'])
        return Response(serializer.data,status=status.HTTP_201_CREATED)
        getPhoneNumberRegistered.get(email=serializer.data['email'])
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def get_access_token(request):
    return 
from django.forms.models import model_to_dict
def fetchToken(user):
    try:
        refresh = RefreshToken.for_user(user)
        # c=CustomUser.objects.get(email=user.email)
        
        # print(model_to_dict(c))
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
    @swagger_auto_schema( operation_description='otp',request_body=LoginSerializer)
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
        
        # request.headers['email']=user.email
        # return get_otp(request,user.email)
        # print(data)
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
from drf_yasg import openapi
header_param = openapi.Parameter('email',openapi.IN_QUERY,description="local header param", type=openapi.IN_BODY)

def get_otp(request,email):#email
       
        try:
            user = CustomUser.objects.get(email=email)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            return Response({"error":"User not registered"},404)
            # CustomUser.objects.create(
            #     email=email,
            # )
            # user = CustomUser.objects.get(email=email)  # user Newly created Model
        user.counter += 1  # Update Counter At every Call
        user.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(email).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        # print(OTP.at(user.counter))
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return  Response({"OTP": OTP.at(user.counter)})  # Just for demonstration

class getPhoneNumberRegistered(APIView):
    # Get to Create a call for OTP

    
    @staticmethod
    # @swagger_auto_schema(manual_parameters=[header_param])
    # @swagger_auto_schema( operation_description='',request_body=OtpSerializer)
    def get(request):#email
        email=request.data['email']
        user=None
        try:
            user=CustomUser.objects.get(email=email)
            if( user is not None):
                print(user.email)
                user.counter+=1
                user.save()
                
                return JsonResponse({'data':OTP.at(user.counter)})
                return Response({'error':'user does not exist'})
            # else:
            #     user=CustomUser.objects.create(email=email)
            #     # user.counter+=1
            #     user.save()
                
            #     return JsonResponse({'data':OTP.at(user.counter)})
        except ObjectDoesNotExist:
            user=CustomUser.objects.create(email=email)
                # user.counter+=1
            user.save()
            
            return JsonResponse({'data':OTP.at(user.counter)})
            return JsonResponse({"error":"object does not exist"})
        except Exception as e:
            print(e)


        print(request.data)


        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(user.email).encode())  # Key is generated
        OTP = pyotp.HOTP(key)
        print(OTP.verify('576486',30))
        otp=OTP.at(1234)

        print(otp)
        # print(OTP.verify(otp,1234))
        print(user.counter)
        newotp=OTP.at(user.counter)
        print(newotp)
        return JsonResponse({'data':newotp,'otp':otp})
        phone=request.body['phone']
        try:
            user = CustomUser.objects.get(email=phone)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            # return JsonResponse({"error":"User not registered"},404)
            CustomUser.objects.create(
                email=phone,
            )
            user = CustomUser.objects.get(email=phone)  # user Newly created Model
        user.counter += 1  # Update Counter At every Call
        user.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        # print(OTP.at(user.counter))
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return  JsonResponse({"OTP": OTP.at(user.counter)})  # Just for demonstration


    # This Method verifies the OTP
 
    @staticmethod
    @swagger_auto_schema( operation_description='otp',request_body=VerifyOtpSerializer)
    def post(request):# email
        email=request.data['email']
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(email).encode())  # Key is generated
        OTP = pyotp.HOTP(key)
        print(OTP.verify(request.data['at'],1234))
        try:
            # otp=(request.data['otp'])
            user=CustomUser.objects.get(email__iexact=request.data["email"])
            if(OTP.verify(int(request.data['otp']),user.counter)):
                user.emailVerified=True
                user.save()
                return Response({"success":"You are authorized"})
            else:
                return JsonResponse({"error":"OTP is wrong"}, status=400)
        except Exception as e:
            print(str(e))
            return JsonResponse({"error":"OTP is wrong"}, status=400)
        # serializers=VerifyOtpSerializer
        # try:
        #     user = CustomUser.objects.get(email__iexact=request.data["email"])
        #     print(user.email)
        #     print(user.counter)
        # except ObjectDoesNotExist:
        #     return Response({"error":("User does not exist")}, status=404)  # False Call

        # keygen = generateKey()
        # key = base64.b32encode(keygen.returnValue(email).encode())  # Generating Key
        # OTP = pyotp.HOTP(key)  # HOTP Modelhotp.at(1401) # => '316439'
        # # print(OTP)
        # try:
        #     if OTP.verify(316439, 140):  # Verifying the OTP
        #         user.isVerified = True
        #         user.save()
        #         return Response({"success":"You are authorised"}, status=200)
        #     else:
        #         return Response({"error":("OTP is wrong")}, status=400)
        # except Exception as e:
        #     return Response(str(e))
class PhoneNumberOTP(APIView):
    def get(self, request, format=None):
        return Response({})
    def post(self, request,format=None):
        return Response({})
class HelloAPi(APIView):
    def get(self, request, pk, format=None):
        return Response({})

def hello(request):
    return JsonResponse({"HELLOV":""},status=200)