from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class FrontPageViewTestCase(TestCase):
    """Test cases for the frontPage view function."""

    def setUp(self):
        """Set up test data before each test method."""
        self.client = Client()
        self.url = reverse("front_page_index")

        # Create test users with different roles
        self.admin_user = User.objects.create_user(
            username="admin_user",
            email="admin@example.com",
            password="testpass123",
            role="administrator",
        )

        self.project_manager_user = User.objects.create_user(
            username="pm_user",
            email="pm@example.com",
            password="testpass123",
            role="project_manager",
        )

        self.regular_user = User.objects.create_user(
            username="regular_user",
            email="user@example.com",
            password="testpass123",
            role="member",
        )

    def test_frontpage_unauthenticated_user(self):
        """Test frontPage view with unauthenticated user."""
        response = self.client.get(self.url)

        # Check response status
        self.assertEqual(response.status_code, 200)

        # Check correct template is used
        self.assertTemplateUsed(response, "frontPage.html")

        # Check context doesn't contain user_role
        self.assertNotIn("user_role", response.context)

    def test_frontpage_authenticated_admin_user(self):
        """Test frontPage view with authenticated administrator user."""
        self.client.login(username="admin_user", password="testpass123")
        response = self.client.get(self.url)

        # Check response status
        self.assertEqual(response.status_code, 200)

        # Check correct template is used
        self.assertTemplateUsed(response, "frontPage.html")

        # Check context contains user_role
        self.assertIn("user_role", response.context)
        self.assertEqual(response.context["user_role"], "administrator")

    def test_frontpage_authenticated_project_manager_user(self):
        """Test frontPage view with authenticated project manager user."""
        self.client.login(username="pm_user", password="testpass123")
        response = self.client.get(self.url)

        # Check response status
        self.assertEqual(response.status_code, 200)

        # Check correct template is used
        self.assertTemplateUsed(response, "frontPage.html")

        # Check context contains user_role
        self.assertIn("user_role", response.context)
        self.assertEqual(response.context["user_role"], "project_manager")

    def test_frontpage_authenticated_regular_user(self):
        """Test frontPage view with authenticated regular user."""
        self.client.login(username="regular_user", password="testpass123")
        response = self.client.get(self.url)

        # Check response status
        self.assertEqual(response.status_code, 200)

        # Check correct template is used
        self.assertTemplateUsed(response, "frontPage.html")

        # Check context contains user_role
        self.assertIn("user_role", response.context)
        self.assertEqual(response.context["user_role"], "member")

    def test_frontpage_get_method_only(self):
        """Test that frontPage view handles GET requests properly."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        # The view should work with other HTTP methods too since it doesn't restrict them
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)

    def test_frontpage_with_superuser(self):
        """Test frontPage view with superuser."""
        User.objects.create_superuser(
            username="superuser",
            email="super@example.com",
            password="testpass123",
            role="administrator",
        )

        self.client.login(username="superuser", password="testpass123")
        response = self.client.get(self.url)

        # Check response status
        self.assertEqual(response.status_code, 200)

        # Check context contains user_role
        self.assertIn("user_role", response.context)
        self.assertEqual(response.context["user_role"], "administrator")

    def test_user_authentication_state_change(self):
        """Test behavior when user authentication state changes."""
        # First, test as unauthenticated
        response = self.client.get(self.url)
        self.assertNotIn("user_role", response.context)

        # Then login and test again
        self.client.login(username="regular_user", password="testpass123")
        response = self.client.get(self.url)
        self.assertIn("user_role", response.context)
        self.assertEqual(response.context["user_role"], "member")

        # Logout and test again
        self.client.logout()
        response = self.client.get(self.url)
        self.assertNotIn("user_role", response.context)
