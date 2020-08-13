from rest_framework import status

from .test_api import TestSetUp

# Create your tests here.


class TestViews(TestSetUp):
    """Testando as views..."""

    def test_registration_without_data(self):
        response = self.client.post(self.login_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_user_sucess(self):
        response = self.client.post(self.login_url,
                                    self.user_data,
                                    format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_token_invalid_data(self):
        response = self.client.post(self.token_url,
                                    self.user_data,
                                    format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_token_user_verified(self):
        self.client.post(self.login_url, self.user_data, format="json")
        response = self.client.post(self.token_url,
                                    self.user_data,
                                    format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
