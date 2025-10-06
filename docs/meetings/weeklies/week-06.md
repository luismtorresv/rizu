---
title: "Weekly: Week 6"
---

## About the meeting

- Date: 2025-08-23
- Time: 14:59-15:25
- Participants: Jerónimo Acosta, Juan Sebastián Jácome, Paula Llanos, Luis Torres
- Recording: [Link to SharePoint][recording]

[recording]: <https://eafit.sharepoint.com/:v:/s/Rizu/Ee2GVEXN3OhBoUIFQc81CosBo89g63FvUcun3kmKyWWT_g?e=cqKBnU>

!!! note "AI-generated content disclaimer"

    The following is an AI-generated summary of the meeting based on the
    transcript.

## OpenStack Installation and Configuration

* Team explored installation on different environments (Azure, VirtualBox),
  identifying hardware requirements and optimizing approaches.
* Luis Miguel and Jeronimo tested installation on Azure; initial VM had
  insufficient RAM, leading them to create a new VM with 8 GB RAM and 2 vCPUs
  for a more suitable setup.
* Paula Ines advanced installation on VirtualBox, evaluating whether to continue
  in that environment or switch to alternatives for efficiency.
* Luis Miguel proposed refining the installation script to exclude unnecessary
  components (e.g., RabbitMQ), aiming for a lighter configuration aligned with
  project needs.

## Horizon Dashboard and Feature Development

* Jeronimo and Paula Ines examined extending Horizon (Django-based) with new
  views and controllers for Terraform integration.
* Jeronimo explained Horizon’s open-source flexibility allows creation of new
  features such as Terraform script integration.
* Luis Miguel confirmed Horizon’s interface is easy to customize (logos,
  colors), enabling adaptation to project requirements.
* Paula Ines raised questions on final platform appearance; Jeronimo clarified
  it would remain similar to Horizon with added Terraform functionality.

## Terraform Integration and Containers

* Juan Sebastian successfully installed Terraform, using the OpenStack provider
  to create a Docker container called “tutorial” with configured ports.
* He shared findings on .tf files, and basic commands like `init` and `build`,
  and will distribute a two-hour tutorial to the group.
* Team discussed strategies for researching Terraform–OpenStack integration,
  with Juan Sebastian continuing investigation on defining resources and
  workflows.

## User Stories and Acceptance Criteria

* Jeronimo and Luis Miguel noted current user stories are too abstract; they
  proposed rewriting them to match technical tasks being executed.
* New stories will cover concrete actions such as creating virtual environments
  and installing OpenStack, making progress more measurable.
* Team acknowledged challenges in drafting acceptance criteria and agreed to
  consult the professor during the next session for guidance.

## Technical and Academic Challenges

* Team identified gaps in networking knowledge, SSH usage, and Terraform
  integration as primary technical hurdles.
* Luis Miguel and Paula Ines flagged the need for more background in cloud
  networking concepts.
* Jeronimo highlighted SSH as a learning priority for advancing OpenStack setup.
* Academic workload (exams, assignments) may temporarily reduce available time,
  but the team remains committed to progressing steadily.

## Preparation for Meeting with León and Demo

* Team agreed to prepare a structured presentation for León, consolidating
  progress and organizing a demo.
* Luis Miguel suggested planning the flow in advance to present a cohesive and
  professional update.
* Members coordinated availability for Monday, deciding to meet in the
  morning/afternoon before Juan Sebastian’s evening exam.

## Follow-up Tasks

* Share Terraform tutorial with group — Juan Sebastian
* Coordinate Monday meeting to prepare León presentation/demo — Jeronimo, team
* Optimize OpenStack installation script by removing unnecessary components —
  Luis Miguel
