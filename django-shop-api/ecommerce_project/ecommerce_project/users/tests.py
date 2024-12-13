from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAuthenticationTests(APITestCase):
    def setUp(self):
        self.register_url = '/api/auth/register/'
        self.login_url = '/api/auth/login/'
        self.refresh_url = '/api/auth/token/refresh/'
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'StrongPassword123!',
            'first_name': 'Test',
            'last_name': 'User'
        }

    def test_user_registration(self):
        """Test user registration endpoint."""
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('username', response.data)
        self.assertIn('email', response.data)
        print("test_user registration success")

    def test_user_login(self):
        """Test user login endpoint."""
        # Register a user first
        self.client.post(self.register_url, self.user_data)

        # Attempt to log in
        response = self.client.post(self.login_url, {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        print("test_user login success")

    def test_token_refresh(self):
        """Test token refresh endpoint."""
        # Register a user first
        self.client.post(self.register_url, self.user_data)

        # Log in to get tokens
        login_response = self.client.post(self.login_url, {
            'username': self.user_data['username'],
            'password': self.user_data['password']
        })
        refresh_token = login_response.data['refresh']

        # Refresh the token
        response = self.client.post(self.refresh_url, {
            'refresh': refresh_token
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        print("test_token refresh success")
