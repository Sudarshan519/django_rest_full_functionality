from rest_framework import serializers
from .models import *
import django.contrib.auth.password_validation as validators
from django.contrib.auth import authenticate
class PhoneSerializer(serializers.Serializer):
    phone=serializers.IntegerField(label="Phone",required=True)
    
# class VerifyOtpSerializer(serializers.Serializer):
#     phone=serializers.IntegerField(label="Phone",write_only=True)
#     otp=serializers.IntegerField(label="Otp")



class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields =  '__all__'
class InvitationSerializer(serializers.ModelSerializer):
    company=CompanySerializer(Company,many=False)
    class Meta:
        model=Invitations
        fields = ['company']#'__all__'
    def to_representation(self, instance):
        data=super(InvitationSerializer,self).to_representation(instance)
        data=data['company']
        return data
    

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields='__all__'
class AcceptInvitationSerializer(serializers.Serializer):
    id=serializers.IntegerField(label='id')
    accept=serializers.BooleanField(label='isAccepted')
    def validate(self, data):
        
        # user = self.context.get("request").user
        id=data['id']
        print(id)
        if id is None:
            raise serializers.ValidationError(
                {'detail': 'Not found.'},
                code=404,
            )
        return data
    