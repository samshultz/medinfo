from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import MedicalInfo
from .forms import MedicalInfoForm

class MedicalInfoFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(first_name="Samuel", 
                         last_name="Taiwo", 
                         username="samshultz", 
                         email="ta@gmail.com",
                         password="reductionism")
        self.factory = RequestFactory()

    def test_that_user_was_saved(self):
        med_info = self.user.medical_info
        med_info.surgery = True
        med_info.save()
        med = MedicalInfo.objects.get(patient=self.user)
        self.assertEqual(med_info, med)

    def test_form_saved(self):
        form = MedicalInfoForm(instance=self.user.medical_info, data={'pacemaker': True})
        print(self.user.medical_info)
        self.assertTrue(form.is_valid())