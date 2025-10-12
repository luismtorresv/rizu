from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from authentication.forms import OpenStackUserRegistrationForm

User = get_user_model()


class LoginViewTestCase(TestCase):
    """Test cases for the login_view function."""

    def setUp(self):
        """Set up test data before each test method."""
        self.client = Client()
        self.url = reverse("login")

        # Create a test user
        self.test_user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            role="user",
        )

    def test_login_view_get_request(self):
        """Test login view returns correct template and form on GET request."""
        response = self.client.get(self.url)

        # Check response status
        self.assertEqual(response.status_code, 200)

        # Check correct template is used
        self.assertTemplateUsed(response, "login.html")

        # Check form is in context
        self.assertIn("form", response.context)

        # Check it's an AuthenticationForm
        from django.contrib.auth.forms import AuthenticationForm

        self.assertIsInstance(response.context["form"], AuthenticationForm)

    def test_login_view_post_valid_credentials(self):
        """Test login view with valid credentials redirects correctly."""
        response = self.client.post(
            self.url, {"username": "testuser", "password": "testpass123"}
        )

        # Check redirect to front page
        self.assertRedirects(response, reverse("front_page_index"))

        # Check user is authenticated
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_view_post_invalid_credentials(self):
        """Test login view with invalid credentials shows error message."""
        response = self.client.post(
            self.url, {"username": "testuser", "password": "wrongpassword"}
        )

        # Check response status (should render login page again)
        self.assertEqual(response.status_code, 200)

        # Check error message is displayed
        messages = list(response.context["messages"])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Invalid username or password")

        # Check user is not authenticated
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_login_view_post_empty_form(self):
        """Test login view with empty form data."""
        response = self.client.post(self.url, {})

        # Should render login page with form errors
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")
        self.assertFalse(response.context["form"].is_valid())

    def test_login_view_already_authenticated_user(self):
        """Test that already authenticated users can still access login page."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(self.url)

        # Should still return 200 (Django doesn't restrict this by default)
        self.assertEqual(response.status_code, 200)


class RegisterViewTestCase(TestCase):
    """Test cases for the register_view function."""

    def setUp(self):
        """Set up test data before each test method."""
        self.client = Client()
        self.url = reverse("register")

    def test_register_view_get_request(self):
        """Test register view returns correct template and form on GET request."""
        response = self.client.get(self.url)

        # Check response status
        self.assertEqual(response.status_code, 200)

        # Check correct template is used
        self.assertTemplateUsed(response, "register.html")

        # Check form is in context
        self.assertIn("form", response.context)

        # Check it's an OpenStackUserRegistrationForm
        self.assertIsInstance(response.context["form"], OpenStackUserRegistrationForm)

    def test_register_view_form_has_required_fields(self):
        """Test that the registration form contains expected fields."""
        response = self.client.get(self.url)
        form = response.context["form"]

        # Check form has required fields
        self.assertIn("username", form.fields)
        self.assertIn("email", form.fields)
        self.assertIn("role", form.fields)
        self.assertIn("password1", form.fields)
        self.assertIn("password2", form.fields)

    def test_register_view_post_invalid_data_password_mismatch(self):
        """Test register view with mismatched passwords."""
        response = self.client.post(
            self.url,
            {
                "username": "newuser",
                "email": "newuser@example.com",
                "password1": "securepass123",
                "password2": "differentpass123",
                "role": "user",
            },
        )

        # Should render register page with form errors
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register.html")
        self.assertFalse(response.context["form"].is_valid())

        # User should not be created
        self.assertFalse(User.objects.filter(username="newuser").exists())

    def test_register_view_post_invalid_data_missing_fields(self):
        """Test register view with missing required fields."""
        response = self.client.post(
            self.url,
            {
                "username": "newuser",
                # Missing email, passwords, and role
            },
        )

        # Should render register page with form errors
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register.html")
        self.assertFalse(response.context["form"].is_valid())

    def test_register_view_post_duplicate_username(self):
        """Test register view with already existing username."""
        # Create a user first
        User.objects.create_user(
            username="existinguser",
            email="existing@example.com",
            password="testpass123",
            role="user",
        )

        # Try to register with same username
        response = self.client.post(
            self.url,
            {
                "username": "existinguser",
                "email": "newemail@example.com",
                "password1": "securepass123",
                "password2": "securepass123",
                "role": "user",
            },
        )

        # Should render register page with form errors
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["form"].is_valid())

        # Should have username error
        self.assertIn("username", response.context["form"].errors)
