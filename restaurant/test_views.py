from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Burger", price=9.99, inventory=5)

    def test_get_menu(self):
        response = self.client.get(reverse('menu-items-list'))  # Adjust name if needed
        self.assertEqual(response.status_code, status.HTTP_200_OK)
