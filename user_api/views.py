from django.shortcuts import render
from .models import *
#Django Rest-Framework imports
from rest_framework.parsers import JSONParser
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins

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

