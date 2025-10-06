---
title: "Client Meeting: Week 10"
---

## About the meeting

- Date: 2025-09-16
- Time: 13:55-14:36
- Participants: León Jaramillo, Jerónimo Acosta, Juan Sebastián Jácome, Paula Llanos, Luis Torres
- Recording: [Link to SharePoint][recording]

[recording]: <https://eafit.sharepoint.com/:v:/s/Rizu/EZj2R9zHw7tCg0Ov6q7JbhIB0iZ910fcEUxDOv-dibQZBg?e=i8oqpD>

!!! note "AI-generated content disclaimer"

    The following is an AI-generated summary of the meeting based on the
    transcript.

## Review of Demo and Feedback

* The professor gave no new feedback beyond what was discussed during the demo.
* No pending questions or concerns after the sprint review.

## Sprint Scope and Planning

* Over the weekend, the team defined the sprint scope, created user stories for
  each member, and assigned task estimates.
* Emphasis on relative estimation rather than fixed hours/days, to keep
  consistency in complexity comparisons.
* A preliminary diagram was shared to show the user’s path before reaching the
  dashboard, still under development but useful to outline project structure.

## Roles and Project Management in OpenStack

* Roles clarified: administrator and member will be used, with a project manager
  subrole able to create projects. Reader role excluded.
* Projects in OpenStack define boundaries for resources and permissions,
  distinguished between user projects and service projects.
* Hierarchical nature of roles was emphasized: higher roles inherit permissions
  of lower ones, relevant for managing access through the interface.

## User Interface and Resource Creation

* Two options for resource creation: API forms for VMs, networks, and routers,
  and a Terraform integration for advanced provisioning.
* The interface will assist Terraform users by displaying data like Project ID
  and available networks.
* Permissions must remain consistent between API and Terraform paths to avoid
  privilege bypass.

## Technical Issues with Floating IPs and SSH

* VMs are being created successfully but cannot be accessed via SSH due to
  floating IP and network configuration issues.
* A bastion host was suggested as a controlled entry point for SSH, improving
  security.
* The team received datacenter credentials and a private IP but no clear
  instructions on usage, requiring follow-up with the responsible professor.

## Resource Control in OpenStack

* OpenStack can limit resource usage per user or project; the team will
  investigate configuration of these quotas.
* Terraform restrictions must align with OpenStack permissions to prevent
  unauthorized resource creation.
* Resource limits are critical to prevent a single user from consuming all
  available capacity.

## Interface Improvements and CRUD Operations

* Plan to expand the interface with CRUD functions for VMs and networks.
* Users will be able to edit, delete, and stop VMs, alongside network
  management.

## User Journey and Documentation

* An embedded user journey was proposed, showing users how to start with the GUI
  and then move to Terraform.
* Technical feasibility in Django is uncertain; alternatives include recording a
  video, extracting a transcript, and producing a user manual with screenshots.

## Next Steps and Coordination

* Next meeting set for two weeks due to EI week.
* Team will send updates and relevant links in the group chat to maintain
  progress between sessions.

## Follow-up Tasks

* **University Infrastructure:** Ask the responsible professor for instructions
  on accessing the university datacenter with provided credentials. (Luis
  Miguel)
* **OpenStack Quotas:** Investigate configuration of resource limits per
  user/project.
* **Interface Localization:** Check if Horizon supports language changes and
  ensure own interface is available in English and Spanish.
* **Terraform Restrictions:** Research whether Terraform can enforce
  OpenStack-based permissions.
* **User Journey Tools:** Explore options for “first time” onboarding journeys
  and evaluate integration into Django.
* **Progress Updates:** Share project updates in the group chat during the
  no-meeting week.
