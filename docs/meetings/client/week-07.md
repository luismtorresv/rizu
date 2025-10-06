---
title: "Client Meeting: Week 7"
---

## About the meeting

- Date: 2025-08-26
- Time: 13:58-14:53
- Participants: León Jaramillo, Jerónimo Acosta, Juan Sebastián Jácome, Paula Llanos, Luis Torres
- Recording: [Link to SharePoint][recording]

[recording]: <https://eafit.sharepoint.com/:v:/s/Rizu/Ee_kTJ-7ppNDs-6f0-QtvhwBMpNQaPgrV13KtiH9eDanVw?e=0l4kgF>

!!! note "AI-generated content disclaimer"

    The following is an AI-generated summary of the meeting based on the
    transcript.

### OpenStack Installation and Configuration
- Luis Miguel, Paula Ines, and the team explained progress to Leon Jaramillo on
  installing OpenStack using different methods, detailing technical challenges
  and solutions, with Juan Sebastian contributing to Terraform integration.
- **Installation Methods:** Luis Miguel and Paula Ines described using both
  Colansible and DevStack. DevStack is lighter and developer-oriented, while
  Colansible is more complete and production-ready.
- **Technical Issues:** The team faced static file loading problems in Horizon
  (CSS) due to accidental overwrites and Apache permission issues. Logs were
  reviewed, and file ownership was adjusted to fix the problem.
- **Infrastructure Requirements:** Minimum requirements discussed were 8–16 GB
  RAM, 40–70 GB disk, and two network interfaces. Performance and costs of Azure
  were compared against local or institutional alternatives.
- **Terraform Integration:** Juan Sebastian confirmed the OpenStack provider for
  Terraform, enabling automated provisioning of private cloud resources.

### Search for University Infrastructure
- Leon Jaramillo suggested the team seek access to university servers,
  recommending contact with Professor Edwin Montoya to request resources and
  avoid high cloud costs.
- **University Contact:** The team agreed to reach out to Edwin Montoya,
  professor of distributed systems, to explore access to university servers.
- **Formal Request:** Leon Jaramillo drafted and sent a formal email to Edwin
  Montoya describing the project and requesting guidance and resources. The team
  will follow up and attempt a direct meeting.
- **Advantages of Local Infrastructure:** Benefits include avoiding cloud costs
  and leaving infrastructure available for future student projects, increasing
  institutional impact.
- **Alternative Options:** If university access is denied, the team considered
  personal hardware, with Luis Miguel offering his computer for deployment.

### Project Projection and Business Plan
- Leon Jaramillo guided the team on institutional and commercial impacts,
  suggesting a business model and positioning the project as a potential VMware
  alternative.
- **Institutional Impact:** The project could serve as a VMware replacement at
  the university, enabling more open infrastructure management and long-term
  academic use.
- **Business Model:** Leon explained viable business models for private cloud
  solutions, where companies save costs by migrating from public clouds to
  self-hosted solutions supported by third parties.
- **Business Plan:** Luis Miguel asked about creating a business plan; Leon
  confirmed its relevance, particularly if offering support and maintenance
  services is considered.

### Infrastructure Testing and Validation
- Luis Miguel and Leon Jaramillo discussed validation strategies, emphasizing
  functional testing and external group participation.
- **Testing Strategies:** Best validation would be allowing other groups to
  deploy on the infrastructure, complemented by resilience, reliability, and
  latency tests. Professors will be consulted for appropriate testing
  methodologies.

## Follow-up Tasks
- **University Infrastructure Request:** Consult Professor Edwin Nelson Montoya
  about accessing a permanent server or VM at the university to deploy the
  private cloud with OpenStack, and specify minimum requirements. (Luis Miguel,
  Paula Ines, Juan Sebastian)
- **Email Communication:** Send Leon Jaramillo the email address of Professor
  Edwin Nelson Montoya and team members’ emails for inclusion in formal
  communication. (Luis Miguel)
- **Technical Specifications:** Verify and define minimum hardware and OS
  requirements for installing OpenStack with Kolla Ansible, and consider
  requesting additional resources if possible. (Luis Miguel, Paula Ines, Juan
  Sebastian)
- **Infrastructure Testing and Validation:** Consult the course professor on
  possible methods for testing infrastructure, including workflows and
  attributes such as resilience and reliability. (Luis Miguel)
