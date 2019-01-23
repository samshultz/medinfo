from django.test import TestCase, RequestFactory
from django.urls import reverse_lazy
from ..context_processors import active_menu


class ActiveMenuContextProcessorTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_active_menu_return_users_for_active_variable(self):
        req = self.factory.get(reverse_lazy('user_list'))
        context_processor = active_menu(req)
        self.assertEqual(context_processor['menu'], 'users')
    
    def test_active_menu_return_statistics_for_active_variable(self):
        req = self.factory.get(reverse_lazy('user_statistics'))
        context_processor = active_menu(req)
        self.assertEqual(context_processor['menu'], 'statistics')

    def test_active_menu_return_home_for_active_variable(self):
        req = self.factory.get(reverse_lazy('user_detail'))
        context_processor = active_menu(req)
        self.assertEqual(context_processor['menu'], 'home')

