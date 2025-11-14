---
title: "Automated Tests"
icon: "material/bird"
---

There was 1 major hiccup when it came to developing End-To-End tests for Rizu: the use of
the university’s own VPN service. Since we wanted to prove that our virtual private cloud
dashboard could be deployed on premise, we requested a VM hosted within the campus
server rack. However, we needed to use a VPN for every connection, halting any attempts at
developing the usual GitHub Action tests that these sorts of applications require.

Therefore we were given 3 paths to choose from:

1. Create an interface that separates the OpenStack-related functions with mock
functions that serve only to return an HTTP Code.

2. Develop tests in another VPC provider such as Azure, AWS or GCP, since their
environments are not closed off by a VPN.

3. Forgo feature/E2E tests.

We initially chose the second option, but due to the VM’s instability inside Azure/AWS, we
failed to develop the tests. So, we gave option one a chance, and developed an interface
that replaces the ‘Builder’ and ‘Util’ functions with mocks.


```python title="Rizu/Openstack/Interface.py"
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
```


We also had to modify our views in Django to coincide with the new interface, and we made
sure to use Django’s own testing commands and files to facilitate testing.
In the end, we managed to develop 14 End-To-End tests that checked the responses of each
of our views, as well as successful executions of our OpenStack connections (using HTTP
codes as metrics):

- Loading into the front page
- User Registration form and processing
- Login Form and Authentication
- Dashboard access and rendering
- Create project as a project manager
- VM creation form and rendering
- Network creation access
- Router creation access
- Storage creation access and rendering
- User profile access
- Joining a project
- Terraform view access
- Dashboard with project selection
- Logout functionality

After running the tests numerous times, we committed them to the repo and created a
GitHub Action so that the End-To-End tests will always run on every Push and PR.

```yaml title=".github/workflows/e2e-tests.yml"
name: End-to-End Tests

on:
    push:
        branches:
            - master
    pull_request:
        branches:
            - master

jobs:
    e2e-test:
        runs-on: ubuntu-latest

        steps:
            - name: Checkout code
              uses: actions/checkout@v4

            - name: Setup Python
              uses: actions/setup-python@v5
              with:
                  python-version: 3.x
                  cache: 'pip'

            - name: Install dependencies
              run: |
                  pip install -r requirements.txt

            - name: Run end-to-end tests
              run: |
                  python manage.py test --settings=Rizu.test_settings runserver.tests.RizuHTTPResponseTests
```

## Automated Testing Strategy

Rizu’s CI job runs `pytest` + `pytest-django` with `--ds=Rizu.test_settings`,
which flips `OPENSTACK_MOCK_MODE` on and routes every builder/utils call through
`Rizu.Openstack.Interface`. That switch means our tests can test authentication,
dashboard, and resource flows without needing the VPN access or real
credentials.

## Legacy Unit Coverage

Early coverage focused on `authentication/tests.py` and `dashboard/tests.py`,
asserting template wiring, role gates, and helper correctness. They were
intentionally simple yet ensured forms validated input, views rendered, and
unauthenticated paths failed loudly—preventing regressions while the UI was
still volatile.

## End-to-End HTTP Runs

The new `runserver/tests.py` suite spins a Django test client to walk the entire
stack: register → login → dashboard → project/network/VM/storage forms →
profile/logout.

Because the mock interface mimics OpenStack builders/utilities, each request
exercises the same code paths as production, giving us deterministic 200/302/500
assertions and surfacing routing or permission slips immediately.

## Results

All HTTP journeys pass, and the faux OpenStack telemetry confirmed no unexpected
calls escaped to the real cloud.
