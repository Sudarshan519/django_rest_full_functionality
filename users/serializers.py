from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
import django.contrib.auth.password_validation as validators
from django.contrib.auth import authenticate


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profileDocuments = serializers.HyperlinkedRelatedField(many=True, view_name='users:profileDocuments', read_only=True)
    class Meta:
        model = CustomUser
        fields = [ 'id', 'email','kyc_updated','emailVerified','profileDocuments'#, 'groups''username','url',
        ]
    def create(self, validated_data):
        return super().create(validated_data)
class ProfileDocumentsSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.email')
    # url = serializers.HyperlinkedIdentityField(view_name="users:users")
    class Meta:
        model= ProfileDocuments
        # fields ='__all__'
        exclude=()
    def perform_create(self, serializer):
            serializer.save(user=self.request.user)
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):   

    class Meta:
        model=CustomUser
        fields=['email','password']
        write_only_fields=['password']

    def validate_password(self, data):
            validators.validate_password(password=data, user=User)
            data=make_password(data)
            return data

class OtpSerializer(serializers.Serializer):
    email=serializers.EmailField(label="Email")
 
    
class VerifyOtpSerializer(serializers.Serializer):
    email=serializers.EmailField(label="Email",write_only=True)
    otp=serializers.IntegerField(label="Otp")
    
class LoginSerializer(serializers.Serializer):  

    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    email = serializers.CharField(
        label="email",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        email = attrs.get('email')
        password = attrs.get('password')
        
        if email and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
            
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs
    

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Banners 
        exclude = ('active', )
        # fields = '__all__'
class TermsAndConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model=TermsAndConditions
        exclude=()


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profession
        # fields=['name_en','statusOfResidenceEn','residenceType']
        exclude=()
class ResidenceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ResidenceType
        exclude=()

class StatusResicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=StatusOfResidence
        exclude=()

class PostalCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostalCode
        exclude=()
import re
class PhoneEmailSerializer(serializers.ModelSerializer):
    phone_email=serializers.CharField()
    def validate_phone_number(self, value):
        # Define the regex pattern for phone number validation
        pattern = r'^\+\d{1,3}-\d{3}-\d{3}-\d{4}$'
        emailpattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        # Apply the regex pattern to the phone number
        if re.match(pattern, value):
            return value
            #raise serializers.ValidationError('Invalid phone number.')
        elif re.match(emailpattern, value):
            return value
        # Return the validated phone number
        raise serializers.ValidationError('Invalid phone/email number.')