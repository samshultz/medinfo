from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    date_of_birth = models.DateField(blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    
    # Admin use this to verify if the person is a doctor so as to 
    # determine the info (s)he gets access to
    is_doctor = models.BooleanField(default=False)

    def __str__(self):
        return "Profile for {} {}".format(self.user.first_name, self.user.last_name)


class MedicalInfo(models.Model):
    """
        Medical Information about A Patient.

        Information About what a patient is currently suffering or has 
        previously suffered from.
    """
    patient = models.OneToOneField(settings.AUTH_USER_MODEL, 
                                   on_delete=models.CASCADE, 
                                   related_name="medical_info")
    surgery = models.BooleanField("Any surgery within the last five years", default=False, blank=True)
    allergies = models.BooleanField("Allergies(including massage oils)", default=False, blank=True)
    epilepsy = models.BooleanField(default=False, blank=True)
    pacemaker = models.BooleanField("Any metal pins or plates as a result of surgery", default=False, blank=True)
    circulatory_problems = models.BooleanField("Any circulatory problems, Thrombosis etc)", default=False, blank=True)
    illness = models.BooleanField("Major Illness/ injury", default=False, blank=True)
    liver_kidney_ailments = models.BooleanField("Liver/Kidney ailments", default=False, blank=True)
    medication = models.BooleanField("Are you currently taking any form of"
                                     "medication(including Homeopathic remedies", default=False, blank=True)
    back_pains = models.BooleanField("Back pains", default=False, blank=True)
    nervous_disorders = models.BooleanField("Nervous disorders", default=False, blank=True)
    blood_born_diseases = models.BooleanField("Blood born diseases (Hep B, AIDS, HIV)", default=False, blank=True)
    reduced_reflexes = models.BooleanField("Reduced reflexes(if known)", default=False, blank=True)
    broken_capillaries = models.BooleanField("Broken capillaries", default=False, blank=True)

    def __str__(self):
        return "{} {}".format(self.patient.first_name, self.patient.last_name)