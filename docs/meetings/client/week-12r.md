---
title: "Client Meeting: Semana de Receso"
---

# Client Meeting: Semana de Receso

## About the meeting

- Date: 2025-10-07
- Time: 14:00-14:30
- Participants: León Jaramillo, Jerónimo Acosta, Juan Sebastián Jácome, Paula
  Llanos, Luis Torres
- Recording: [Link to SharePoint][recording]

[recording]: <https://eafit.sharepoint.com/:v:/s/Rizu/EU-v8Rp1jKpNutNNc2bzAe8BgX5MRO4c_6QqR0wKCLRDgA>

!!! note "AI-generated content disclaimer"

    The following is an AI-generated summary of the meeting based on the
    transcript.

## Wiki and Sprint Presentation

jeronimo updated leon on the restructured sprint 2 wiki, organized by luis.
Although the presentation isn’t finished, the team defined two goals: displaying
the phone interface and deploying a virtual machine with OpenStack. leon
suggested adding a direct link to the backlog in the wiki.

## Backlog Review

The backlog structure and task distribution have improved. jeronimo noted the
user story section was moved out of the main backlog. leon advised clarifying
this in the presentation and explaining the current use of Django’s standard
login system.

## Deployment and DCA Access

jeronimo reported that OpenStack was deployed on a university virtual machine,
but outgoing network traffic remains blocked. He contacted freddy, the DCA
admin, to request changes and plans to follow up. The infrastructure uses a
VMware-like system and requires VPN access.

## Platform Features

jeronimo demonstrated current platform capabilities: user and project creation,
network and router setup, and role-based dashboards for *project managers* and
*users*. paula ines confirmed she hasn’t yet tested the new project creation
flow.

## Terraform Interface Development

juan sebastián and jeronimo presented progress on the Terraform interface. They
shifted from predefined fields to a free-text editor for direct script input and
are still working on full integration.

## Testing Environment

Due to VPN restrictions on the university VM, automated tests will be run on
Azure, ensuring smoother integration and deployment.

## Sprint Goals

leon emphasized that the key milestone for sprint 2 is enabling virtual machine
creation in OpenStack, forming the foundation for later Terraform and service
integration.

# Follow-Up Tasks

* **jeronimo:** Add a direct backlog link in the wiki.
* **jeronimo:** Remind freddy to enable outbound traffic on the university VM.
* **jeronimo:** Coordinate with freddy to activate the project URL for public
  access.
* **jeronimo, luis:** Run automated tests on Azure instead of the university VM.
* **juan sebastián:** Update the Terraform interface to allow free-text code
  input.
* **jeronimo and team:** Prioritize OpenStack virtual machine creation in sprint
  2.
