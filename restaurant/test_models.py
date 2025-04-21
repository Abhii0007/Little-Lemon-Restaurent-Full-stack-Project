from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_menu_item_str(self):
        item = Menu.objects.create(name="Pizza", price=12.99, menu_item_description=10)
        self.assertEqual(str(item), "Pizza")
