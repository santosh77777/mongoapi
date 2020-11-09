from django.db import models
# Create your models here.


class Badge(models.Model):
    badge_id = models.IntegerField(null=True, blank=True)
    name = models.CharField( max_length=250)

    def __str__(self):
        return self.name

class Achivement(models.Model):
    achivement_id = models.IntegerField(null=True, blank=True)
    name = models.CharField( max_length=250)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    certificate_id = models.IntegerField(null=True, blank=True)
    name = models.CharField( max_length=250)

    def __str__(self):
        return self.name


class UpcomingCertificate(models.Model):
    upcoming_certificate_id = models.IntegerField(null=True, blank=True)
    name = models.CharField( max_length=250)

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    user_id = models.IntegerField()
    name = models.CharField( max_length=250)
    dob = models.DateField(auto_now=False, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    collaboration_ready = models.BooleanField(default=True)
    school_name = models.CharField( max_length=250)
    activity_id = models.IntegerField(null=True, blank=True)
    mentor_id = models.IntegerField(null=True, blank=True)
    no_of_classes = models.IntegerField(null=True, blank=True)
    badges = models.ForeignKey(Badge, related_name='badge', on_delete=models.CASCADE, null=True)
    achivements = models.ForeignKey(Achivement, related_name='achivement', on_delete=models.CASCADE, null=True)
    certificates = models.ForeignKey(Certificate, related_name='certificate', on_delete=models.CASCADE, null=True)
    upcoming_certificates = models.ForeignKey(UpcomingCertificate, related_name='upcoming_certificate', on_delete=models.CASCADE, null=True)
    created_by = models.CharField( max_length=250, null=True, blank=True)
    modified_by = models.CharField( max_length=250, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name



# this model Stores the data of the Phones Verified
class phoneModel(models.Model):
    Mobile = models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)   # For HOTP Verification

    def __str__(self):
        return str(self.Mobile)
