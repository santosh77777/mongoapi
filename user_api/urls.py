from django.urls import path, include
from . import views


urlpatterns = [
    #path('', views.StudentProfileDetail.as_view()),
    path('api/students/', views.StudentProfileDetail.as_view()),
    path('api/student/<int:id>/', views.StudentProfileDetail.as_view()),
    path("verify/<phone>/", views.getPhoneNumberRegistered.as_view(), name="OTP Gen"),
    

]