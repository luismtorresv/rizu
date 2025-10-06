---
title: "Weekly: Week 7"
---

## About the meeting

- Date: 2025-08-30
- Time: 15:01-15:45
- Participants: Jerónimo Acosta, Juan Sebastián Jácome, Paula Llanos, Luis Torres
- Recording: [Link to SharePoint][recording]

[recording]: <https://eafit.sharepoint.com/:v:/s/Rizu/ERQCDRa3u15AoAdgyxxtpCIBem-hvEmga1fdQvMAZoAIzg?e=y0Z9XE>

!!! note "AI-generated content disclaimer"

    The following is an AI-generated summary of the meeting based on the
    transcript.

## Project Refactor and New Architecture

* Team (Jeronimo, Luis Miguel, Juan Sebastian, Paula Ines) agreed to refactor
  the project to meet integrator requirements, designing a new architecture
  based on Django and OpenStack with Terraform integration.
* Jeronimo explained the previous project didn’t meet requirements, so the team
  will build a Django dashboard for students with limited cloud knowledge,
  integrating Terraform scripts to create private clouds in OpenStack.
* Proposed architecture: client-server model, with a monolithic server hosting
  OpenStack projects and the Django dashboard, with possible server separation
  for security and robustness (Luis Miguel, Jeronimo).
* Luis Miguel confirmed an existing repository can be reused. Roles were
  distributed: each member will take user stories, Paula Ines focusing on
  frontend design (CSS, Bootstrap).
* Development will begin in Django, with tasks distributed and all members
  researching technical topics, especially Terraform–OpenStack integration.

## Professor Feedback

* Luis Miguel and Jeronimo reviewed professor’s suggestions on installation
  simplicity, permission management, hardware changes, and Terraform use.
  Actions were set to clarify and align project with feedback.
* Installation should be simple: team will explore automation of OpenStack and
  app deployment via Bash or Python scripts.
* Django includes permission handling; team will study documentation for proper
  integration in the dashboard.
* On hardware modification: team concluded this likely refers to changing
  instance resources in OpenStack. Jeronimo will confirm with professor.
* Terraform recommended for private cloud creation: team will explore
  Django–OpenStack API connection followed by Terraform script execution. Juan
  Sebastian will investigate Terraform’s capabilities in this context.

## Technical Integration: Django, OpenStack, Terraform

* Jeronimo and Luis Miguel led discussion on authentication, data flow, and
  private cloud creation.
* Jeronimo explained OpenStack authentication through Keystone and possible use
  of django-openstack-auth. Documentation and configuration examples were
  reviewed.
* Team debated whether to create private clouds via OpenStack API or Terraform
  scripts. Decision aligned with professor’s recommendation to prioritize
  Terraform.
* Juan Sebastian tasked with investigating Terraform’s capabilities in OpenStack
  (subnets, VMs, storage, authentication, script execution).
* Team discussed user interface: whether users could edit generated Terraform
  scripts directly or through a simplified interface. Priority is ease of use
  for non-technical users.

## Business Plan, Test Cases, and Software Quality

* Luis Miguel and Jeronimo addressed requirements for business plan, test cases,
  and software quality. Tasks were distributed.
* Business plan will adapt from previous work, targeting users with limited
  cloud experience.
* Team will consult professor about test cases, expecting next class to cover
  this topic.
* Luis Miguel proposed adding a standards file and static analysis tool to the
  repository, documenting quality measures from the start.

## Testing, Resources, and Technical Constraints

* Team discussed testing options and resource limitations (public IPs,
  virtualization).
* Jeronimo and Luis Miguel suggested using VirtualBox and local virtualization
  for testing while external resources are arranged.
* Main constraint: lack of public IPs. Team considered NAT and coordination with
  Edwin/university for needed resources.
* Limitations such as inability to run multiple private clouds on one OpenStack
  instance and dependency on university resources will be documented.

## Follow-up Tasks

* Clarify project requirement #3 (admin ability to add/change hardware) with
  León — Jeronimo
* Investigate Terraform’s scope in private cloud creation for OpenStack — Juan
  Sebastian
* Initialize Django repository and share with team — Luis Miguel
* Send urgent follow-up message to León on project viability — Jeronimo
* Collect all Terraform resources (videos, links) into one place — Luis Miguel
* Ask professor about required test cases — Jeronimo
* Investigate Django–OpenStack interaction and Terraform integration details —
  Jeronimo
* Support frontend development with CSS/Bootstrap — Paula Ines
