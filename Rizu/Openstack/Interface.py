"""
OpenStack Mode Switcher

This module provides a unified interface that switches between real and mock
OpenStack operations based on Django settings. This allows seamless testing
without modifying view code.
"""

from django.conf import settings
from typing import Any


def get_openstack_utils():
    """
    Get the appropriate OpenStack Utils class based on test mode.
    Returns mock version during testing, real version in production.
    """
    if getattr(settings, "OPENSTACK_MOCK_MODE", False):
        from Rizu.Openstack.MockUtils import MockOpenStackUtils

        print("🧪 Using Mock OpenStack Utils")
        return MockOpenStackUtils
    else:
        from Rizu.Openstack.Utils import OpenStackUtils

        return OpenStackUtils


def get_openstack_builders():
    """
    Get the appropriate OpenStack Builders class based on test mode.
    Returns mock version during testing, real version in production.
    """
    if getattr(settings, "OPENSTACK_MOCK_MODE", False):
        from Rizu.Openstack.MockBuilders import MockOpenStackBuilders

        print("🧪 Using Mock OpenStack Builders")
        return MockOpenStackBuilders
    else:
        from Rizu.Openstack.Builders import OpenStackBuilders

        return OpenStackBuilders


def is_mock_mode() -> bool:
    """Check if we're running in mock OpenStack mode"""
    return getattr(settings, "OPENSTACK_MOCK_MODE", False)


def get_mock_config() -> dict:
    """Get mock OpenStack configuration"""
    return getattr(settings, "MOCK_OPENSTACK_CONFIG", {})


class OpenStackInterface:
    """
    Unified interface for OpenStack operations that automatically
    switches between mock and real implementations based on settings.
    """

    @property
    def Utils(self):
        """Get Utils class (mock or real based on settings)"""
        return get_openstack_utils()

    @property
    def Builders(self):
        """Get Builders class (mock or real based on settings)"""
        return get_openstack_builders()

    def get_connection(self, **kwargs):
        """Get OpenStack connection (mock or real)"""
        return self.Utils.get_openstack_connection(**kwargs)

    def is_testing(self) -> bool:
        """Check if we're in test mode"""
        return is_mock_mode()


# Create a singleton instance
openstack = OpenStackInterface()
