from rest_framework import serializers
from .models import *
import django.contrib.auth.password_validation as validators
from django.contrib.auth import authenticate
class PhoneSerializer(serializers.Serializer):
    phone=serializers.IntegerField(label="Phone",required=True)
    
class VerifyOtpSerializer(serializers.Serializer):
    phone=serializers.IntegerField(label="Phone",write_only=True)
    otp=serializers.IntegerField(label="Otp")