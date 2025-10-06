---
title: "Weekly: Week 8"
---

## About the meeting

- Date: 2025-09-06
- Time: 14:57-16:06
- Participants: Jerónimo Acosta, Juan Sebastián Jácome, Paula Llanos, Luis Torres
- Recording: [Link to SharePoint][recording]

[recording]: <https://eafit.sharepoint.com/:v:/s/Rizu/ERKQKB_nwi9Pmk5cKBHTwvcBA40cRrDNx6K85F_O65swYw?e=9h6PlA>

!!! note "AI-generated content disclaimer"

    The following is an AI-generated summary of the meeting based on the
    transcript.

## Git Workflow and Pull Requests
- A structured process was agreed for managing branches and pull requests. Paula
  will prepare the PR for CSS changes, following best practices for title and
  description. Luis Miguel will review before merging to keep the main branch
  stable.

## User Stories and Backlog
- Jeronimo drafted the user stories for sprint 1 and requested Luis Miguel’s
  support with acceptance criteria.
- The team identified dependencies between stories and agreed to clean the
  backlog, removing duplicates or unnecessary tasks.

## OpenStack Infrastructure
- A simplified flow was defined for the first sprint: the user only enters the
  project name, and the system automatically creates the project, public
  network, private network, and router.
- The team established the use of the OpenStack SDK (Keystone and Neutron) for
  authentication, network and router creation, and visualization in the Rizu
  dashboard.
- Luis Miguel will validate network and router creation using the SDK in Python.
  Paula will handle visualization in the dashboard. Jeronimo will lead
  integration and project creation. Juan Sebastian will connect the view with
  the Django controller.

## Product and User Experience
- The team decided that the custom dashboard will replace Horizon as the
  visualization point, simplifying the user experience.
- Advanced technical details (e.g., IP ranges) will not be requested in this
  phase, prioritizing accessibility.

## Business Plan and Documentation
- Luis Miguel will write sections 1, 2, and 3 of the business plan. Jeronimo and
  Paula will collaborate on later sections.
- The wiki documentation task remains pending assignment.

## Testing and Validation
- Unit and functional tests will be prioritized to validate infrastructure.
- Horizon will be used to verify that created resources are functional.
- The dashboard will provide clear feedback to the user about created resources.

## Follow-up
- Paula: CSS pull request and dashboard visualization using the SDK.
- Luis Miguel: Validate OpenStack SDK, networks, routers, business plan sections
  1–3, support on Django user system.
- Jeronimo: Integration, project creation from Django, SDK documentation,
  general coordination.
- Juan Sebastian: View–controller connection in Django.

## Other Points
- Professor Luis Miguel Mejía will be invited to Tuesday’s weekly to coordinate
  directly with León.
- Rizu-Playtesting-3 on Azure should be deleted as it contains no relevant data.
