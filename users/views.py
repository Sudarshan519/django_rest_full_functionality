import datetime
from django import views
from django.contrib.auth.models import User, Group
from rest_framework.parsers import JSONParser
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
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(email):
        print(datetime.datetime.now())
        return str(email) + str(datetime.datetime.now()) + "Some Random Secret Key"




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
        getPhoneNumberRegistered.get(request),#,email=serializer.data['email'])
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
            "cuser":model_to_dict(user),
            # "model":model_to_dict(user),
            "email":user.email,
            "ekyc_verified":user.kyc_updated(),
            "isEmailVerified":user.isVerified,
            "access_token":str(refresh.access_token),
            "refresh_token":str(refresh),
            # "profile_updated":user.profile_updated
        })
    except Exception as e :
        return  e
 
class LoginView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)
    @swagger_auto_schema( operation_description='otp',request_body=LoginSerializer)
    def post(self, request, refreshformat=None):
        serializer = LoginSerializer(data=request.data,
            context={ 'request': request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        data=fetchToken( user)
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
header_param = openapi.Parameter('email',openapi.IN_HEADER,description="local header param", type=openapi.IN_BODY)

class getPhoneNumberRegistered(APIView):
    # Get to Create a call for OTP

    
    @staticmethod
    @swagger_auto_schema(manual_parameters=[header_param])
    # @swagger_auto_schema( operation_description='',request_body=OtpSerializer)
    def get(request):#email
        email=request.headers['email']
        try:
            user = CustomUser.objects.get(email=email)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            CustomUser.objects.create(
                email=email,
            )
            user = CustomUser.objects.get(email=email)  # user Newly created Model
        user.counter += 1  # Update Counter At every Call
        user.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(email).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        print(OTP.at(user.counter))
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return  Response({"OTP": OTP.at(user.counter)})  # Just for demonstration


    # This Method verifies the OTP
 
    @staticmethod
    @swagger_auto_schema( operation_description='otp',request_body=VerifyOtpSerializer)
    def post(request,):# email
        # print(email)
        email=request.data['email']
        # serializers=VerifyOtpSerializer
        try:
            user = CustomUser.objects.get(email__iexact=request.data["email"])
        except ObjectDoesNotExist:
            return Response(serializers.ErrorDetail("User does not exist"), status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(email).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["otp"], user.counter):  # Verifying the OTP
            user.isVerified = True
            user.save()
            return Response({"success":"You are authorised"}, status=200)
        return Response({"error":("OTP is wrong")}, status=400)