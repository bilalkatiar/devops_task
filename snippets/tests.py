from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


# Create your tests here.
class UserTest(APITestCase):

    def setUp(self):
        self.success_register_data = {
            "username": "admin@xyz.com2",
            "first_name": "bilal",
            "last_name": "katiar",
            "email": "bilalb@gmail.com",
            "is_active": True,
            "is_staff": True,
            'password': "abcjklxyz"
        }

        self.fail_register_data = {
            "first_name": "bilal",
            "last_name": "bilal",
            "is_active": True,
            "is_staff": True,
        }

    def test_register_user_api_success(self):
        url = reverse('user-list')
        response = self.client.post(url, self.success_register_data)
        assert response.status_code == 201

    def test_register_user_api_fail(self):
        url = reverse('user-list')
        response = self.client.post(url, self.fail_register_data)
        assert not response.status_code == 201

    def test_register_success_user(self):
        url = reverse('user-list')
        _ = self.client.post(url, self.success_register_data)
        user = User.objects.get(email=self.success_register_data.get('email'))

        assert user

    def test_login_success_user(self):
        url = reverse('user-list')
        response = self.client.post(url, self.success_register_data)

        url = reverse('rest_framework:login')
        response = self.client.post(url, self.success_register_data)

        user = User.objects.get(email=self.success_register_data.get('email'))

        assert user

    def test_login_fail_user(self):
        url = reverse('rest_framework:login')
        response = self.client.post(url, self.fail_register_data)

        user = User.objects.filter(email=self.success_register_data.get('email')) or None
        print(response.status_code)

        assert not user

