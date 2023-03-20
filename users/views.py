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


# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(phone): 
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

@swagger_auto_schema(tags=['user'],method='post', operation_description='',request_body=RegisterSerializer)
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
        print(email)
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
