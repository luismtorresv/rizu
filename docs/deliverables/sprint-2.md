---
title: "Sprint 2: MVP v2"
icon: "material/motorbike"
---

> “Would it save you a lot of time if I just gave up and went mad now?”
>
> ― Douglas Adams, _The Hitchhiker’s Guide to the Galaxy_

<!----------------------------------------------------------------------------->

## Usability Tests Protocol

<!-- Planear las pruebas de usabilidad con los usuarios finales que van a
utilizar el sistema, usando como referencia el “Protocolo de Pruebas de
Usabilidad”. -->

<!-- OJO: Solo se deben planear las pruebas; la ejecución de estas se
realizará durante el Sprint 3. -->

The main objective of the usability tests is to evaluate the usability of the
Rizu web console to ensure an effective, efficient, and satisfactory experience
for end users managing OpenStack resources. The tests will validate key user
flows in the MVP v2 interface and identify friction points affecting
comprehension, navigation, and task completion.

### Test 1: Account Creation and Login

**Task:**
 Create a new account and log into the platform.

**Hypothesis:**
 Users will be able to sign up and log in without requiring
external guidance. Field labeling and validation feedback will be sufficient to
guide completion.

**Metrics:**

- Time to complete (minutes)
- Success rate (%)
- Number of input errors
- Post-task satisfaction (1–5 scale)

**Research Question:**
 Can new users easily understand the registration and
authentication process?

### Test 2: Project Selection and Navigation

**Task:**
 Access the dashboard after login and select an existing project to
manage.

**Hypothesis:**
 The project list and selection mechanism are intuitive, with no
ambiguity regarding where to start managing cloud resources.

**Metrics:**

- Time to locate and select project
- Success rate (%)
- Navigation errors (wrong clicks, confusion events)
- User-reported clarity of layout (1–5)

**Research Question:**
 Do users understand how to locate and access a specific
project from the dashboard?

### Test 3: Network and Router Creation

**Task:**
 Create a network and attach a router using the provided interface.

**Hypothesis:**
 The configuration flow for network and router creation follows a
logical sequence and requires minimal technical prior knowledge.

**Metrics:**

- Task completion time
- Number of retries/errors
- Success rate (%)
- User confidence rating (1–5)

**Research Question:**
 Can users successfully configure networking components
without prior OpenStack experience?

### Test 4: Virtual Machine Deployment

**Task:**
 Launch a new virtual machine (instance) within a selected project and
network.

**Hypothesis:**
 The VM creation wizard provides clear guidance and prevents
misconfiguration through validation and defaults.

**Metrics:**

- Time to launch instance
- Error count (e.g., missing fields, invalid selections)
- Completion rate (%)
- Satisfaction level (1–5)

**Research Question:**
 Do users understand how to deploy a VM and verify its
status after creation?

### Test 5: Overall Workflow Comprehension

**Task:**
 Perform a complete end-to-end flow: login → select project → create
network → launch VM → verify deployment.

**Hypothesis:**
 Users can complete the full workflow with limited confusion and
minimal external reference.

**Metrics:**

- Total time for full flow
- Task success rate (%)
- Total number of errors
- Overall satisfaction (System Usability Scale or 1–5 average)

**Research Question:**
 Does the integrated workflow provide a coherent and
seamless experience across tasks?

### Measurement and Reporting

All tests will be conducted using screen recording and direct observation.
Quantitative metrics will be complemented with short qualitative interviews
post-session to identify usability pain points and improvement priorities.

<!----------------------------------------------------------------------------->

## Automated Testing

<!-- El proyecto debe tener una estrategia de pruebas automáticas que
garanticen la calidad y el buen funcionamiento de la aplicación. -->

<!-- Documentar la estrategia que se va a usar usando la siguiente tabla:
    (ver tabla) -->

<!-- Todas las funcionalidades entregadas deben estar cubiertas por al menos
una prueba automática. -->

The automated testing strategy ensures that all delivered functionalities in the
Rizu web console are validated for correctness, internal consistency, and user
flow reliability. The current scope of automated testing focuses exclusively on
Rizu’s own application layer (views, forms, routing, and permission logic)
without interacting directly with live OpenStack APIs. The goal is to maintain
code stability and predictable behavior across releases by verifying that all
implemented views and components respond correctly to expected and edge-case
inputs.

Automated tests are executed continuously as part of the development workflow
using **pytest** and **pytest-django**. Each push or pull request triggers the
test suite, ensuring regressions are caught before merging into main. Coverage
centers on the application’s authentication, project management, and dashboard
modules, which together represent the primary user interaction paths.

### Test Coverage Matrix

| Functionality                                 | Type of Test                   | Rationale                                                                                                                                                                                                               |
| --------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **User Authentication (Login, Registration)** | Unit and Integration Tests     | Authentication is a critical entry point. Unit tests validate form handling, field validation, and credential verification, while integration tests confirm end-to-end request/response behavior and redirection logic. |
| **Project Creation and Access Control**       | Integration and Scenario Tests | Project-level permissions and roles (manager vs. user) require validation across multiple components (views, permissions, templates). Scenario tests confirm correct restriction and authorization behavior.            |

### Implementation Notes

- The current automated suite consists mainly of **unit** and **integration**
  tests built with **pytest-django**.
- **Unit tests** focus on individual views, forms, and permission decorators,
  validating template usage, form fields, and error handling.
- **Integration tests** verify that views and templates work together, checking
  for correct redirections, access control, and context rendering.
- Existing unit tests (as shown) cover all authentication, registration, and
  dashboard-related views.
- The test suite runs automatically in CI for every commit, maintaining baseline
  assurance that recent changes have not broken authentication, routing, or
  permission logic.
- Scenario and E2E tests will be added using tools such as **pytest-django** to
  simulate real user workflows (login → project → network → VM).
