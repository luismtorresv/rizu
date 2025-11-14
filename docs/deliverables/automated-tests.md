---
title: "Automated Tests"
icon: "material/bird"
---

There was one major hiccup when developing end-to-end tests for Rizu: every
OpenStack call required the university VPN. To deploy the dashboard on-prem, we
requested a campus VM, but that meant GitHub Actions could not reach the
cluster. We considered three paths:

1. Create an interface that separates the OpenStack-related functions with mock
   implementations that return deterministic responses.
2. Develop tests in another VPC provider such as Azure, AWS, or GCP, where the
   environments are publicly accessible.
3. Forgo feature/E2E tests altogether.

Option two failed because the cloud VM proved unstable, due to configurations
mismatch, so we invested in option one and shipped a switchable interface that
replaces the original builder/util helpers with mocks whenever tests run.

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

After swapping our views to consume the interface, we leaned on Django’s test
runner to script fourteen HTTP journeys that validate both page rendering and
the mocked OpenStack operations:

- Loading the front page
- User registration form and processing
- Login form and authentication
- Dashboard access and rendering
- Project creation as a project manager
- VM creation form and rendering
- Network creation access
- Router creation access
- Storage creation access and rendering
- User profile access
- Joining a project
- Terraform view access
- Dashboard with project selection
- Logout functionality

Once the suite stabilized, we added it to CI so every push and PR exercises the
stack in mock mode.

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

Rizu’s CI job runs `pytest` and `pytest-django` with
`--settings=Rizu.test_settings`, which flips `OPENSTACK_MOCK_MODE` on and routes
every builder/utils call through `Rizu.Openstack.Interface`. That switch lets us
verify authentication, dashboard, and resource flows without VPN access or real
credentials.

## Legacy Unit Coverage

Early coverage lived in `authentication/tests.py` and `dashboard/tests.py`,
asserting template wiring, role gates, and helper correctness. They ensured
forms validated input, views rendered, and unauthenticated paths failed
loudly—preventing regressions while the UI was still volatile.

## End-to-End HTTP Runs

The newer `runserver/tests.py` suite spins a Django test client to walk the
entire stack—register → login → dashboard → project/network/VM/storage forms →
profile/logout. Because the mock interface mirrors the OpenStack
builders/utilities, each request exercises the same code paths as production,
yielding deterministic 200/302/500 assertions and surfacing routing or
permission slips immediately.

## Results

All HTTP journeys pass, and the faux OpenStack telemetry confirmed no unexpected
calls escaped to the real cloud. The mock-first approach also keeps feedback
loops fast enough to run in every CI cycle.

## Personal Opinion

Working on these tests felt like finally seeing behind the curtain. At first we
thought “automation” was just a fancy checkbox, but once we scripted the flows
and saw them pass without touching the VPN, it clicked: testing is basically
future-us saying thanks for not breaking everything. It was messy, we had to
improvise with mocks, yet the moment the CI run finished in green we knew we
weren’t guessing anymore—we were actually sure.
