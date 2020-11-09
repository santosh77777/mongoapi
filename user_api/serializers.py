from rest_framework import serializers
from .models import *


class BadgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Badge
        fields = '__all__'

class AchivementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Achivement
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Certificate
        fields = '__all__'

class UpcomingCertificateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UpcomingCertificate
        fields = '__all__'


class StudentProfileSerializer(serializers.ModelSerializer):
    badge = BadgeSerializer(many=True, read_only=True, write_only=False)
    achivement = AchivementSerializer(many=True, read_only=True, write_only=False)
    certificate = CertificateSerializer(many=True, read_only=True, write_only=False)
    upcoming_certificate = UpcomingCertificateSerializer(many=True, read_only=True, write_only=False)



    class Meta:
        model = StudentProfile
        fields = '__all__'



