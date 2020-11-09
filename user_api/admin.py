from django.contrib import admin
from .models import *
#from django_mongoengine import mongo_admin as admin
#Register your models here.

admin.site.register(StudentProfile)
admin.site.register(Badge)
admin.site.register(Achivement)
admin.site.register(Certificate)
admin.site.register(UpcomingCertificate)