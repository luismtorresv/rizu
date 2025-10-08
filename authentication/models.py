from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# Abstract user already comes with the username, email,first_name and last_name, password,
# and a status (is_active, is_staff, is_superuser) attributes.
class OpenStackUser(AbstractUser):

    # to quote the explanation: "In Django, when you define choices, the first value ('admin') is what’s stored in the database,
    # and the second ('Admin') is the human-readable label shown in forms/admin."
    ROLE_CHOICES = (
        ("admin", "Administrator"),
        ("project_manager", "Project Manager"),
        ("member", "User"),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="member")
    openstack_password = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["role"],
                condition=models.Q(role="admin"),
                name="unique_administrator_constraint",
            )
        ]
