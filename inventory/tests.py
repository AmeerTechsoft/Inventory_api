# inventory/tests.py
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from .models import Item, Supplier

class ItemAPITestCase(APITestCase):

    def setUp(self):
        # Create a user and token for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create initial data for testing
        self.item = Item.objects.create(
            name="Test Item",
            description="This is a test item",
            price="10.99"
        )
        self.supplier = Supplier.objects.create(
            name="Test Supplier",
            contact_information="123 Test St"
        )
        self.supplier.items.add(self.item)

    def test_create_item(self):
        url = '/api/items/'
        data = {
            "name": "New Item",
            "description": "This is a new test item",
            "price": "15.99"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "New Item")

    def test_view_item(self):
        url = f'/api/items/{self.item.id}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Item")

    def test_update_item(self):
        url = f'/api/items/{self.item.id}/'
        data = {
            "name": "Updated Item",
            "description": "This is an updated test item",
            "price": "12.99"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Item")

    def test_delete_item(self):
        url = f'/api/items/{self.item.id}/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Item.objects.filter(id=self.item.id).exists())

    def test_view_item_suppliers(self):
        url = f'/api/items/{self.item.id}/suppliers/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Test Supplier")

class SupplierAPITestCase(APITestCase):

    def setUp(self):
        # Create a user and token for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create initial data for testing
        self.item = Item.objects.create(
            name="Test Item",
            description="This is a test item",
            price="10.99"
        )
        self.supplier = Supplier.objects.create(
            name="Test Supplier",
            contact_information="123 Test St"
        )
        self.supplier.items.add(self.item)

    def test_create_supplier(self):
        url = '/api/suppliers/'
        data = {
            "name": "New Supplier",
            "contact_information": "456 New St",
            "items": [self.item.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "New Supplier")

    def test_view_supplier(self):
        url = f'/api/suppliers/{self.supplier.id}/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Supplier")

    def test_update_supplier(self):
        url = f'/api/suppliers/{self.supplier.id}/'
        data = {
            "name": "Updated Supplier",
            "contact_information": "789 Updated St",
            "items": [self.item.id]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Supplier")

    def test_delete_supplier(self):
        url = f'/api/suppliers/{self.supplier.id}/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Supplier.objects.filter(id=self.supplier.id).exists())

    def test_view_supplier_items(self):
        url = f'/api/suppliers/{self.supplier.id}/items/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Test Item")
