---
title: "Automated Tests"
icon: "material/bird"
---

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
