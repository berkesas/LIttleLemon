from django.test import TestCase
from restaurant.models import MenuItem, Booking
from restaurant.views import MenuItemsView
from django.http import request, response
from rest_framework.test import APIClient, force_authenticate
from django.contrib.auth.models import User


class MenuItemsViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        MenuItem.objects.create(
            title="Lemon", price=50, inventory=60)
        MenuItem.objects.create(
            title="IceCream", price=80, inventory=100)

    def test_getall(self):
        response = self.client.get('/restaurant/api/menuitems/')
        self.assertEqual(response.content.decode(),
                         '[{"title":"Lemon","price":"50.00","inventory":60},{"title":"IceCream","price":"80.00","inventory":100}]')

    def test_getone(self):
        last_id = MenuItem.objects.last().id
        response = self.client.get('/restaurant/api/menuitem/'+str(last_id))
        self.assertEqual(response.content.decode(),
                         '{"title":"IceCream","price":"80.00","inventory":100}')


class BookingViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        user = User.objects.create_user(
            username='testuser', email='test@littlelemon.com', password='secret')
        user.save()
        self.user = user

    def test_booking_unauthenticated(self):
        response = self.client.get('/restaurant/api/bookings/tables/')
        self.assertEqual(response.content.decode(),
                         '{"detail":"Authentication credentials were not provided."}')

    def test_booking_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/restaurant/api/bookings/tables/')
        self.assertEqual(response.content.decode(),
                         '[]')


class IndexViewTest(TestCase):
    def test_index(self):
        response = self.client.get('/restaurant/')
        self.assertIn("Capstone Project", response.content.decode())
