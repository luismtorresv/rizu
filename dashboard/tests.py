from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateVMViewTestCase(TestCase):
    """Test cases for the create_vm view function."""

    def setUp(self):
        """Set up test data before each test method."""
        self.client = Client()
        self.url = reverse("create_vm")

        # Create a test user
        self.test_user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            role="member",
        )

    def test_create_vm_get_unauthenticated(self):
        """Test create_vm view GET request without authentication."""
        response = self.client.get(self.url)

        # Should still return 200 (no auth required in view)
        self.assertEqual(response.status_code, 200)

        # Check correct template is used
        self.assertTemplateUsed(response, "create_vm.html")

    def test_create_vm_get_authenticated(self):
        """Test create_vm view GET request with authenticated user."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(self.url)

        # Check response status
        self.assertEqual(response.status_code, 200)

        # Check correct template is used
        self.assertTemplateUsed(response, "create_vm.html")


class CreateProjectViewTestCase(TestCase):
    """Test cases for the create_project view function."""

    def setUp(self):
        """Set up test data before each test method."""
        self.client = Client()
        self.url = reverse("create_project")

        # Create test users with different roles
        self.project_manager = User.objects.create_user(
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

    def test_create_project_get_as_project_manager(self):
        """Test create_project view GET request as project manager."""
        self.client.login(username="pm_user", password="testpass123")
        response = self.client.get(self.url)

        # Check response status
        self.assertEqual(response.status_code, 200)

        # Check correct template is used
        self.assertTemplateUsed(response, "create_project.html")

    def test_create_project_get_as_regular_user(self):
        """Test create_project view GET request as regular user (not allowed)."""
        self.client.login(username="regular_user", password="testpass123")
        response = self.client.get(self.url)

        # Should return 200 with error message
        self.assertEqual(response.status_code, 200)

        # Check error message in response
        self.assertContains(response, "You are not allowed to create projects.")


class CreateNetworkViewTestCase(TestCase):
    """Test cases for the create_network view function."""

    def setUp(self):
        """Set up test data before each test method."""
        self.client = Client()
        self.url = reverse("create_network")

        # Create a test user
        self.test_user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            role="member",
        )

    def test_create_network_get_request(self):
        """Test create_network view GET request."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(self.url)

        # Check response status
        self.assertEqual(response.status_code, 200)

        # Check correct template is used
        self.assertTemplateUsed(response, "create_network.html")

    def test_create_network_get_unauthenticated(self):
        """Test create_network view GET request without authentication."""
        response = self.client.get(self.url)

        # Should still return 200 (no auth required in view)
        self.assertEqual(response.status_code, 200)

        # Check correct template is used
        self.assertTemplateUsed(response, "create_network.html")


class CreateRouterViewTestCase(TestCase):
    """Test cases for the create_router view function."""

    def setUp(self):
        """Set up test data before each test method."""
        self.client = Client()
        self.url = reverse("create_router")

        # Create a test user
        self.test_user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
            role="member",
        )

    def test_create_router_get_request(self):
        """Test create_router view GET request."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(self.url)

        # Check response status
        self.assertEqual(response.status_code, 200)

        # Check correct template is used
        self.assertTemplateUsed(response, "create_router.html")

    def test_create_router_get_unauthenticated(self):
        """Test create_router view GET request without authentication."""
        response = self.client.get(self.url)

        # Should still return 200 (no auth required in view)
        self.assertEqual(response.status_code, 200)

        # Check correct template is used
        self.assertTemplateUsed(response, "create_router.html")


class InitialsHelperTestCase(TestCase):
    """Test cases for the _initials helper function."""

    def test_initials_with_full_name(self):
        """Test _initials with a full name (first and last)."""
        from dashboard.views import _initials

        result = _initials("John Doe")
        self.assertEqual(result, "JD")

    def test_initials_with_single_name(self):
        """Test _initials with a single name."""
        from dashboard.views import _initials

        result = _initials("Madonna")
        self.assertEqual(result, "M")

    def test_initials_with_three_names(self):
        """Test _initials with three names (only first two should be used)."""
        from dashboard.views import _initials

        result = _initials("John Paul Smith")
        self.assertEqual(result, "JP")

    def test_initials_with_empty_string(self):
        """Test _initials with empty string."""
        from dashboard.views import _initials

        result = _initials("")
        self.assertEqual(result, "PR")

    def test_initials_with_none(self):
        """Test _initials with None."""
        from dashboard.views import _initials

        result = _initials(None)
        self.assertEqual(result, "PR")

    def test_initials_with_extra_spaces(self):
        """Test _initials with extra spaces in name."""
        from dashboard.views import _initials

        result = _initials("  John   Doe  ")
        self.assertEqual(result, "JD")

    def test_initials_with_lowercase(self):
        """Test _initials converts to uppercase."""
        from dashboard.views import _initials

        result = _initials("john doe")
        self.assertEqual(result, "JD")

    def test_initials_with_mixed_case(self):
        """Test _initials with mixed case."""
        from dashboard.views import _initials

        result = _initials("JoHn DoE")
        self.assertEqual(result, "JD")
