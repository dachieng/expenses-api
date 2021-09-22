from rest_framework.test import APITestCase
from authentication.models import User


class TestUserModel(APITestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username='dorcas', email='oloodorcas99@gmail.com', password="teddy@123")

        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'oloodorcas99@gmail.com')
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            username='dorcas', email='oloodorcas99@gmail.com', password="teddy@123")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'dorcas')
        self.assertTrue(user.is_staff)

    def test_username_not_provided(self):
        self.assertRaises(ValueError, User.objects.create_user, username="",
                          email="oloodorcas99@gmail.com", password="teddy@123")

    def test_email_not_provided(self):
        self.assertRaises(ValueError, User.objects.create_user,
                          username="dorcas", email="", password="teddy@123")

    def test_is_staff(self):
        self.assertRaises(
            ValueError, User.objects.create_superuser, username="dorcas", email="oloodorcas99@gmail.com", password="teddy@123", is_staff=False)

    def test_check_superuser(self):
        self.assertRaises(ValueError, User.objects.create_superuser, username="dorcas",
                          email="oloodorcas99@gmail.com", password="teddy@123", is_superuser=False)
