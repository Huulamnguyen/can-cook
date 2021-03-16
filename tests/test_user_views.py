"""User View tests."""
from unittest import TestCase
from app import create_app

class UserViewTestCase(TestCase):
    """Test views for users."""

    def setUp(self):
        """Create test client"""

        self.app = create_app('testing')
        self.client = self.app.test_client()

    def tearDown(self):
        response = super().tearDown()
        return response

    def test_homepage(self):
        """Test homepage"""
        with self.client as c:
            response = c.get('/')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('Homepage', html)