from django.test import TestCase, RequestFactory
from restaurant.models import MenuItem
from restaurant.views import MenuItemsView
from django.http import request, response


class MenuItemsViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        MenuItem.objects.create(
            title="Lemon", price=50, inventory=60)
        # MenuItem.objects.create(
        #     title="IceCream", price=80, inventory=100)

    def test_getall(self):
        request = self.factory.get('/restaurant/items')
        response = MenuItemsView.as_view()(request)
        self.assertEqual(response.content,
                         '{"title": "Lemon", "price": "50", inventory: 60}')
