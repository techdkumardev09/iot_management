from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from app.models import Device, TelemetryData

class UserRegistrationViewTest(APITestCase):
    def test_user_registration(self):
        url = '/register/'
        data = {'username': 'test_user', 'password': 'test_password', 'role': 'LEV_OPERATOR'}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)
        
        user = get_user_model().objects.get(username='test_user')
        self.assertTrue(user.check_password('test_password'))

class DeviceViewSetTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test_user', password='test_password')
        self.client.force_authenticate(user=self.user)

    def test_create_device(self):
        url = '/app/devices/'
        data = {'name': 'Test Device', 'description': 'Test Description', 'telemetry_data': {'key': 'value'}}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Device.objects.count(), 1)
        self.assertEqual(Device.objects.first().name, 'Test Device')

    def test_list_devices(self):
        url = '/app/devices/'
        Device.objects.create(name='Device 1', description='Description 1')
        Device.objects.create(name='Device 2', description='Description 2')
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

class TelemetryDataViewSetTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test_user', password='test_password')
        self.client.force_authenticate(user=self.user)

    def test_create_telemetry_data(self):
        device = Device.objects.create(name='Test Device', description='Test Description')
        url = f'/app/telemetry/'
        data = {'device_id': device.id, 'timestamp': '2022-01-01T00:00:00Z', 'value': 42.0}
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TelemetryData.objects.count(), 1)
        self.assertEqual(TelemetryData.objects.first().value, 42.0)

    def test_list_telemetry_data(self):
        device = Device.objects.create(name='Test Device', description='Test Description')
        url = f'/app/telemetry/'
        TelemetryData.objects.create(device_id=device.id, timestamp='2022-01-01T00:00:00Z', value=42.0)
        TelemetryData.objects.create(device_id=device.id, timestamp='2022-01-02T00:00:00Z', value=55.0)
        
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
