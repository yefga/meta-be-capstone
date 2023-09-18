from django.test import TestCase
from ..models import Menu

class MenuTest(TestCase):
    def test_add_new_menu(self):
        new_menu_item = Menu.objects.create(
            id=6,
            title="Lemon Pie",
            price=12.99,
            inventory=20,
        )

        retrieved_menu_item = Menu.objects.get(title="Lemon Pie")
        self.assertEqual(str(new_menu_item), str(retrieved_menu_item))