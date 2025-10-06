---
title: "Client Meeting: Week 8"
---

## About the meeting

- Date: 2025-09-02
- Time: 13:57-14:58
- Participants: León Jaramillo, Jerónimo Acosta, Juan Sebastián Jácome, Paula Llanos, Luis Torres
- Recording: [Link to SharePoint][recording]

[recording]: <https://eafit.sharepoint.com/:v:/s/Rizu/EcBPsayvu_JLhcn-wcbfYEYBQOxnrJTUb-7LIaGMUDp7Vw?e=02Yeak>

!!! note "AI-generated content disclaimer"

    The following is an AI-generated summary of the meeting based on the
    transcript.

## Project Redefinition and Feedback

* After feedback from Luis Miguel and Leon, the team redefined the project’s
  focus. Instead of modifying Horizon, they proposed building a simplified
  dashboard for private cloud management, balancing automation with Terraform
  and ease of use for non-expert users.
* Luis Miguel highlighted that the initial Horizon modification was too simple
  for the expected scope.
* The new dashboard proposal was presented to both Luis Miguel and Leon, who
  gave feedback and suggestions.
* Leon emphasized the importance of defining a clear scope with specific sprint
  deliverables and aligning with OpenStack’s API to ensure academic and
  institutional relevance.

## Technical Progress: OpenStack Setup

* The team installed OpenStack using kolla-ansible on Azure with Ubuntu 24.04.
* Challenges included compatibility issues, nested virtualization requirements,
  and networking/IP configuration.
* Core services installed: Glance, Nova, Neutron, and Horizon, with additional
  modules considered for later.
* Paula created a custom guide and scripts to automate installation, adding
  missing steps beyond official documentation.

## Sprint 1 Planning

* Main goal: enable the creation of a functional private cloud through the
  dashboard and OpenStack API.
* Terraform integration will be deferred to later sprints; priority is direct
  API use.
* Leon requested EAFIT branding on the dashboard for institutional relevance.
* Initial allocated resources: 16 GB RAM and 76 GB storage. The team agreed to
  begin with this setup and request more if necessary.

## Technical Challenges and Strategy

* Connection between the dashboard and OpenStack, especially networking and VM
  creation, was identified as a major challenge.
* Leon recommended an iterative approach: start with VM creation, then expand to
  additional features depending on effort and value.

## Collaboration with the University

* The professor in charge enabled server space for deployment.
* The team now has access to university infrastructure, though the allocated
  space may be limited. Requests for additional resources will be made if
  needed.

## Follow-up Tasks

* **Define Dashboard Scope:** Document which OpenStack services will be
  manageable via the Django interface for Sprint 1. (Paula, team)
* **Deploy OpenStack at University:** Use the assigned servers, validate
  available space, and request more resources if required. (Paula)
* **Branding:** Customize the interface with EAFIT identity. (Paula, team)
* **Resolve VM Connection Issues:** Investigate and fix OpenStack VM
  connectivity problems before the first delivery. (Paula)
* **Client Communication:** Confirm available resources with the professor and
  align infrastructure expectations. (Paula, team)
