from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from ..models import MedicalInfo, Profile
# from ..forms import MedicalInfoForm


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('samshultz', 
                                             'admin@admin.com', 
                                             'red12345',
                                             first_name="Sam",
                                             last_name="Taiwo")
        self.profile = Profile(user=self.user)
    
    def test_profile_object_return_correct_str_representation(self):
        first_name = self.user.first_name
        last_name = self.user.last_name
        self.assertEqual(str(self.profile), 
                         'Profile for {} {}'.format(first_name, last_name))
        

class MedicalInfoTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('samshultz', 
                                             'admin@admin.com', 
                                             'red12345',
                                             first_name="Sam",
                                             last_name="Taiwo")
    
    def test_medical_info_object_was_created(self):
        self.assertEqual(str(self.user.medical_info), "Sam Taiwo")
    
    def test_medical_info_str_representation(self):
        med_info = MedicalInfo.objects.get(patient=self.user)
        self.assertEqual(str(med_info), "Sam Taiwo")
        