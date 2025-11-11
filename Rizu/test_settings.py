"""
Test Settings for Rizu Application

This settings file is used during testing to enable mock OpenStack mode
and bypass real OpenStack connections. This allows testing when VPN/network
access to OpenStack is not available.
"""

from .settings import *
import os

# Override settings for testing
DEBUG = True

# Test database - use in-memory SQLite for faster tests
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Password validation - disable for faster user creation in tests
AUTH_PASSWORD_VALIDATORS = []


# Disable migrations for faster test setup
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


MIGRATION_MODULES = DisableMigrations()

# Enable mock OpenStack mode
OPENSTACK_MOCK_MODE = True

# Mock OpenStack configuration
MOCK_OPENSTACK_CONFIG = {
    "default_project": "test-project",
    "default_user_role": "member",
    "simulate_delays": False,  # Set to True to simulate OpenStack delays
    "fail_rate": 0.0,  # Percentage of operations that should fail (0.0 = never fail)
}

# Logging configuration for tests
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "WARNING",
        },
        "Rizu": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
}

# Suppress OpenStack SDK warnings in tests
import warnings

warnings.filterwarnings("ignore", module="openstack")

# Email backend for testing
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Cache configuration for testing
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

# Static files handling in tests
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# Security settings relaxed for testing
SECRET_KEY = "test-secret-key-only-for-testing"
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = []

print("🧪 Test settings loaded - Mock OpenStack mode enabled")
