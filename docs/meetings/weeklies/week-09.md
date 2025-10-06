---
title: "Weekly: Week 9"
---

## About the meeting

- Date: 2025-09-13
- Time: 14:55-16:22
- Participants: Jerónimo Acosta, Juan Sebastián Jácome, Paula Llanos, Luis Torres
- Recording: [Link to SharePoint][recording]

[recording]: <https://eafit.sharepoint.com/:v:/s/Rizu/EV4coKfFL9tDu9R687MQkfcBsaxk_Cvvk3O9uLaPfOamDw?e=nIcKJn>

!!! note "AI-generated content disclaimer"

    The following is an AI-generated summary of the meeting based on the
    transcript.

## Feedback on Presentation

* Professor highlighted improvements in structure and English use compared to
  the previous presentation.
* Suggestions: take detailed notes of feedback, keep the app simple but not
  overly basic, and add a user journey to replace the need for a manual.

## Project Scope

* Application: interface for private cloud deployment with OpenStack and
  Terraform, aimed at new developers and SMEs.
* Current features: project creation, networks/routers, API and Terraform
  integration.
* Future additions: object storage, databases, image management, volumes, and
  flavors via Nova and Glance.
* Users: admins with full control, standard users limited to assigned projects.
* UI: homepage, dashboard, project creation, Terraform interface, login managed
  by server credentials.

## Code Quality and Tools

* Use Black for automatic formatting.
* Automate testing with minimum score requirement before merges.
* Replace requirements.txt with Poetry for dependency management.

## Merge Conflict Resolution

* Conflicts occur when two branches edit the same section.
* Options: resolve in GitHub editor or locally, ensuring functional code before
  merging.

## Next Steps

* Add OpenStack installation guide to README with issues found.
* Design and implement interactive user journey.
* Define roles and permissions for admin vs standard users.
* Enforce formatting and linting with Black and Poetry, block merges on errors.
* Document merge resolution procedure.
* Schedule meeting to write user stories and tasks.
