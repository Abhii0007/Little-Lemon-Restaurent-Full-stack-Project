from django.test import TestCase
from django.urls import reverse

class MenuTests(TestCase):
    def test_menu_list_status(self):
        response = self.client.get(reverse('menu-list'))
        self.assertEqual(response.status_code, 200)
