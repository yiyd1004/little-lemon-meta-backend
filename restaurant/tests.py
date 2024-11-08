from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuItemsView
from rest_framework.test import RequestsClient

# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=40, inventory=100)
        self.assertEqual(item, 'IceCream : 40')

class MenuItemsView(TestCase):
    def test_menu_response(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/restaurant/menu-items')

        assert response.status_code == 200
    
    def test_menu_item(self):
        client = RequestsClient()
        response = client.get('http://127.0.0.1:8000/restaurant/menu-items/1')

        self.assertEqual(
            response.data,
            {
                'id': 1,
                'title': 'Pasta',
                'price': '10.00',
                'inventory': 15
            }
        )