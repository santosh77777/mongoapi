from django.shortcuts import render
from .models import *
#Django Rest-Framework imports
from rest_framework.parsers import JSONParser
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
#phonemodel imports
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from .models import phoneModel
import base64

# Create your views here.

class StudentProfileDetail(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
	serializer_class = StudentProfileSerializer
	queryset = StudentProfile.objects.all()


	lookup_field = 'id'

	def get(self, request, id=None):

		if id:
			return self.retrieve(request)
		else:
			return self.list(request)


	def post(self, request):
		return self.create(request)


	def put(self, request, id=None):
		return self.update(request, id)


	def delete(self, request, id):
		return self.destroy(request, id)



#Mobile OTP Logic
# This class returns the string needed to generate the key
class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"


class getPhoneNumberRegistered(APIView):
    # Get to Create a call for OTP
    @staticmethod
    def get(request, phone, *args, **kwargs):
        try:
            serializer_mobile = PhoneModelSerializer
            Mobile = phoneModel.objects.get(Mobile=phone)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            phoneModel.objects.create(
                Mobile=phone,
            )
            serializer_mobile = PhoneModelSerializer
            Mobile = phoneModel.objects.get(Mobile=phone)  # user Newly created Model
        Mobile.counter += 1  # Update Counter At every Call
        Mobile.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        print(Mobile.counter)
        print(OTP.at(Mobile.counter))
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return Response({"text": "Your Current OTP and Current Counter", "OTP": OTP.at(Mobile.counter), "Counter" : Mobile.counter}, status=200)  # Just for demonstration

    # This Method verifies the OTP
    @staticmethod
    def post(request, phone, *args, **kwargs):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = pyotp.HOTP(key)  # HOTP Model
        print(Mobile.counter)
        print(OTP.at(Mobile.counter))
        if OTP.verify(OTP.at(Mobile.counter), Mobile.counter):  # Verifying the OTP
            Mobile.isVerified = True
            Mobile.save()
            otp = OTP.at(Mobile.counter)
            number = Mobile.Mobile
            return Response(f"You are OTP {otp} for mobile number {number} is Verified", status=200)
        return Response("OTP is wrong", status=400)




	