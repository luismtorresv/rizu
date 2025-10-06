---
title: "Client Meeting: Week 5"
---

## About the meeting

- Date: 2025-08-12
- Time: 14:01-14:40
- Participants: León Jaramillo, Jerónimo Acosta, Juan Sebastián Jácome, Paula Llanos, Luis Torres
- Recording: [Link to SharePoint][recording]

[recording]: <https://eafit.sharepoint.com/:v:/s/Rizu/EQhms6B6r-5ApgE4EqbFTa8BI9tG95MoNESgQN5ojZRN9g?e=tUHd89>

!!! note "AI-generated content disclaimer"

    The following is an AI-generated summary of the meeting based on the
    transcript.

## Project Objectives and Tools

* Goal: Enable users to create resources in a private cloud using OpenStack,
  either through a management console or Terraform scripts.
* OpenStack: Core platform for managing VMs, storage, and networks.
* Terraform: Industry-standard IaC tool; allows programmatic provisioning.
  OpenTofu considered as open-source alternative.
* First Sprint: Create a VM using both the console and Terraform.

## Licensing and Alternatives

* Terraform: Now under IBM, no longer open source but still free.
* OpenTofu: Open-source alternative; recommended to support both for
  flexibility.

## Web Interface Decisions

* Framework: Team free to use Django or others.
* Interfaces: Evaluate existing OpenStack GUIs (Horizon, Skyline) before
  building from scratch.

## Recommendations

* Explore OpenStack services and tools (1–2 hours).
* Prioritize VM creation before expanding features.
* Strengthen cloud knowledge via courses (e.g., AWS Educate).
* Use infrastructure diagrams for documentation.

## Follow-up

* Research OpenStack capabilities.
* Investigate customizing Horizon/Skyline.
* Share URLs and repos in group chat.
* Complete AWS Educate “Cloud 101.”
