from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(
            username='user2',
            password='lemon@123!'
        )
        
        self.pizza = Menu.objects.create(id=10, title='Lemon Lime Soda', price=12.99, inventory=10)
        self.burger = Menu.objects.create(id=11, title='Lime Keech', price=8.99, inventory=5)
        self.pasta = Menu.objects.create(id=12, title='Lemon Meringue Pasta', price=15.99, inventory=10)
    
    def loginAsTestUser(self) -> None:
        self.client.login(username='user2', password='lemon@123!')
    
    def test_view_authentication(self) -> None:
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.loginAsTestUser()
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_getall(self):
        self.loginAsTestUser()
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)