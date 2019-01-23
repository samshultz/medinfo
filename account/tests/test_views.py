from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from ..models import Profile 


class UserRegistrationViewTest(TestCase):

    def setUp(self):
        self.user_data = {'username': 'LeoCee', 'first_name': 'Leo',
                     'last_name': 'Cee', 'email': 'lc@mail.com',
                     'password1': 'ert34r251', 'password2': 'ert34r251'}
    def test_user_was_created_successfully(self):
        resp = self.client.post(reverse_lazy('signup'), data=self.user_data)

        self.assertEqual(User.objects.get(id=1).username, 'LeoCee')
    
    def test_profile_object_was_created_for_user(self):
        resp = self.client.post(reverse_lazy('signup'), data=self.user_data)
        self.assertTrue(User.objects.filter(id=1).exists())
    
    def test_view_redirects_after_signup(self):
        resp = self.client.post(reverse_lazy('signup'), data=self.user_data)
        self.assertRedirects(resp, reverse_lazy('user_detail'))


class UserDetailEditViewTest(TestCase):

    def setUp(self):
        self.browser = self.client
        self.user = User.objects.create_user('samshultz', 
                                             'admin@admin.com', 
                                             'red12345',
                                             first_name="Sam",
                                             last_name="Taiwo")
        self.profile = Profile.objects.create(user=self.user)
        
    def test_forms_were_saved_successfully(self):
        self.browser.login(username='samshultz', password='red12345')
        
        form_data = {
            'first_name': 'Samuel', 'last_name': "Kelster", 
            'email': 'user@admin.com', 'date_of_birth': '2015-2-19',
            'surgery': True, 'circulatory_problems': True, 'occupation': 'Musician',
        }
        resp = self.browser.post(reverse_lazy('user_detail'), data=form_data)
        
        user = User.objects.get(username='samshultz')
        
        self.assertEqual(user.first_name, 'Samuel')
        self.assertEqual(user.profile.occupation, 'Musician')
        self.assertTrue(user.medical_info.surgery)
        self.assertTemplateUsed(resp, "account/users/display.html")

    def test_non_authenticated_users_redirected(self):
        resp = self.browser.get(reverse_lazy('user_detail'))
        self.assertEqual(resp.status_code, 302)


class StatisticalDetailsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('samshultz', 
                                             'admin@admin.com', 
                                             'red12345',
                                             first_name="Sam",
                                             last_name="Taiwo")

    def test_view_returns_status_code_of_200(self):
        client = self.client
        login = client.login(username='samshultz', password='red12345')
        resp = client.get(reverse_lazy('user_statistics'))
        self.assertEqual(resp.status_code, 200)

    def test_correct_html_was_used_for_rendering(self):
        client = self.client
        login = client.login(username='samshultz', password='red12345')
        resp = client.get(reverse_lazy('user_statistics'))

        self.assertTemplateUsed(resp, 'account/users/statistical_details.html')

    
    def test_correct_variables_in_context(self):
        client = self.client
        login = client.login(username='samshultz', password='red12345')
        resp = client.get(reverse_lazy('user_statistics'))

        self.assertIn('allergies_chart', resp.context)
        self.assertIn('major_illness_chart', resp.context)
        self.assertIn('different_conditions_chart', resp.context)

    def test_redirects_when_not_logged_in(self):
        resp = self.client.get(reverse_lazy('user_statistics'))
        self.assertEqual(resp.status_code, 302)
