from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


# Create your tests here.
class UserTest(APITestCase):

    def setUp(self):
        success_register_data = {
            "username": "admin@xyz.com2",
            "first_name": "Sadaqatullah",
            "last_name": "Noonari",
            "email": "sadaqatullah.noonari@gmail.com",
            "is_active": True,
            "is_staff": True,
        }

        fail_register_data = {
            "first_name": "Sadaqatullah",
            "last_name": "Noonari",
            "is_active": True,
            "is_staff": True,
        }

    def test_register_success_user(self):
        url = reverse('patient-register')
        response = self.client.post(url, self.patient_correct_data)
