---
title: "Sprint 0: Product Definition"
icon: "material/rocket-launch"
---

## Product Definition

### Problem and Solution

> "Don't worry. There will be new problems."
>
> —Slavoj Žižek

#### Context

Before the advent of cloud computing platforms, software projects were usually
deployed on the hardware owned by an organization. These hardware resources were
managed by the Information Technology department, usually the person acting as
system administrator or "sysadmin".

This approach, while simple enough for common use cases, is prone to fall short
of requirements as time goes on. In other words, it _does not scale well_.

Developers wanting to deploy their applications were constrained by the current
available resources of their organization and/or the sysadmin's willingness to
allocate the resources needed. Moreover, the inability to quickly allocate more
machines as needed, further restricted the system's capacity to handle a growing
number of requests.

Trying to address these issues, engineers at web companies proposed cloud
computing as a reliable alternative to the on-premises model, while introducing
a flexible pay-as-you-go pricing that cut costs.

As of 2023, it was estimated that the market size for public Infrastructure as a
Service was around 133 billion US dollars (according to
[Statista](https://www.statista.com/topics/2739/cloud-infrastructure-as-a-service/#statisticChapter)).
In 2025, it was expected to grow by around 25% (_ibid_).

As time went on, however, new problems arose.

#### The Problem

Flocks of businesses transitioned to off-premises infrastructure managed by
platforms such as Amazon Web Services or Google Cloud Platform. As these
platforms gained more footing in the market, customers started to realize that
they had made themselves depend on these companies to run their businesses or
even offer their services. In addition, as cloud infrastructure platforms
diversified, their pricing tiers became more complicated to grasp. Breaking down
the increasing cloud costs to management became burdensome, and some companies
started moving back to the on-premises model.

**That's where Rizu comes in.**

#### The Solution

Rizu is our proposed alternative for small and medium businesses that want to
have physical control of their infrastructure while taking advantage of a
virtual cloud-like experience.

Naturally, there are already similar projects that implement similar
functionalities (some of these are mentioned further down this document). Rizu
strives to simplify the process of creating a private a cloud by providing a
simpler interface that interacts with bare-metal solutions such as Apache
Cloudstack™. As the saying goes, there are many like it, but this one is ours.


### Project Members

| Member                        | Email                       | Role(s)                 |
| :---------------------------- | :-------------------------- | :---------------------- |
| Jerónimo Acosta Acevedo       | `jacostaa1 at eafit.edu.co` | Architect, Scrum Master |
| Paula Inés Llanos López       | `pillanosl at eafit.edu.co` | UI/UX, Testing          |
| Luis Miguel Torres Villegas   | `lmtorresv at eafit.edu.co` | Programmer              |
| Juan Sebastián Jácome Burbano | `jsjacomeb at eafit.edu.co` | Programmer, UI/UX       |

### Target Audience

![Context diagram.](assets/sprint-0/rizu-context_diagram.png)

- **User (Developer/DevOps Engineer):** The user is the end client who directly
consumes the resources of the private cloud. Their main need is to deploy and
manage infrastructure quickly and easily, such as virtual machines (VMs),
networks, storage, and databases.

- **System Administrator:** The System Administrator is responsible for the
operation, maintenance, and monitoring of the Rizu platform. They identify
errors, and generate reports that are key for better decision-making. They also
oversee the proper operation of the integrations with Terraform, OpenTofu, and
OpenStack.

- **Terraform and OpenTofu:** Terraform and OpenTofu are "Infrastructure as
Code" software tools that automate the deployment and management of
infrastructure through configuration scripts. They are like a bridge between
Rizu and OpenStack.

- **OpenStack:** OpenStack is an open source cloud computing infrastructure
software that we implement to build and manage Rizu. It provides core
infrastructure orchestration services such as virtual machine provisioning
(Nova), network management (Neutron), and storage (Cinder, Swift).

- **Rizu(Private Cloud System):** Rizu is the central system that connects
Terraform, OpenTofu and OpenStack. Its main function is to offer an intuitive
user interface that automates infrastructure deployment and management.


### Interaction with the Solution

| Client                                                              | Sysadmin                                                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| ![Flowchart for Client.](assets/sprint-0/rizu-flowchart-client.jpg) | ![Flowchart for System Administrator ("sysadmin").](assets/sprint-0/rizu-flowchart-sysadmin.jpg) |

### Glossary

- **Private Cloud:** A cloud computing environment dedicated to a single
organization. In a private cloud, all resources (CPU, Storage etc.) are isolated
and in the control of one organization.

- **OpenStack:** An open-source software platform for building and managing
cloud computing infrastructure, often described as Infrastructure-as-a-Service
(IaaS). It provides a set of tools for managing and provisioning compute,
storage, and networking resources, enabling users to create and manage private,
public, and hybrid clouds. Essentially, it allows organizations to build their
own cloud environments using open standards and technologies.

- **IaaS (Infrastructure as a Service):** A cloud computing model where you rent
virtualized computing resources like servers, storage, and networking from a
provider.

- **Infrastructure as Code (IaC):** The managing and provisioning of
infrastructure through code instead of manual processes. With IaC, configuration
files are created that contain your infrastructure specifications, which makes
it easier to edit and distribute configurations.

- **OpenTofu:** An infrastructure as code tool that lets you define both cloud
and on-prem resources in human-readable configuration files that you can
version, reuse, and share.

- **Virtual Machine (VM):** An isolated computing environment with its own CPU,
memory, network interface, and storage, created from a pool of hardware
resources. VMs can emulate endless arrangements of operating systems on the same
physical hardware.

- **Networking:** In a cloud environment, a network typically consists of
several interconnected virtual machines or instances that are hosted on various
physical servers within a data center. These instances can communicate with each
other over a virtual network, which is created and managed by the cloud
provider.

- **Pipelines (CI/CD):** A method in which raw data is ingested from various
data sources, transformed and then ported to a data store, such as a data lake
or data warehouse, for analysis.

- **On-demand self-service:** A consumer can unilaterally provision computing
capabilities, such as server time and network storage, as needed automatically
without requiring human interaction with each service provider.

- **Resource pooling:** The provider’s computing resources are pooled to serve
multiple consumers using a multi-tenant model, with different physical and
virtual resources dynamically assigned and reassigned according to consumer
demand. Customers don’t know the exact resource location but may choose a
general region (e.g., country, state, or datacenter). Resources include storage,
processing, memory, and network bandwidth.


## Requirements Specification

### Functional Requirements
We set up a meeting to discuss an initial approach to the project with our
client. It was held on July 29th at 2:30 PM, and despite some initial hiccups
due to a faulty connection, all team members were present and able to
participate and ask questions. Thanks to this, we ended up outlining the initial
requirements for both the first and second sprints. After completing some
initial formalities, which included setting up future meetings, we proceeded to
outline the crucial functionalities that our project would require. Our client
described the main elements, which included:

- Private Cloud creation.
- VM, DB, and Storage creation.
- Networking.
- Pipelining.
- IaaS architecture.

These core requirements would later turn into Epics, and most user stories would
fall under their umbrella. Regarding physical and tangible evidence, please
refer to the private drive where all evidence is stored.

### Existing Projects
There were few programs which offered the same list of functionalities as ours,
but we did find a couple which showcased the viabilily of the solution, as well
as giving us an outside perspective into the inner-workings of building a web
interface.

- **RedHat**

    RedHat is an implementation of the Openstack functionalities, funneled
    through a web interface that's designed to be more intuitive than the basic
    management interface that Openstack offers. It is implemented by a variety
    of services that control its computing, storage, and networking resources.
    It can also provision resources, although the method through which it does
    so is unavailable to us at the current moment. RedHat is the closest
    software to our proposed solution, so taking a look at it is paramount to
    the success of this project.

    ![Horizon Interface.](assets/sprint-0/redhat-management-interface.png)

- **Horizon**

    Horizon is the OpenStack solution to its own lack of an intuitive management
    console. The core benefit that Horizon offers is the direct connectivity
    with the source program. Besides that, Horizon promises Core Support,
    Extensible and scalable design, consistent performance, and a stable and
    usable API and interface.

    ![Horizon Interface.](assets/sprint-0/horizon-management-interface.png)


## User Story Mapping and Product Backlog

### Story Mapping

![Proposed user story mapping.](assets/sprint-0/rizu-user_story_mapping.jpg)

### Backlog

![Backlog](assets/sprint-0/rizu-backlog.png)

### Sprint 1 Planning

![Sprint 1](assets/sprint-0/rizu-sprint-1-user_stories.png)

## Architecture

### Scope
The MVP Scope of our private cloud platform focuses on delivering the essential
functionality that allows users to easily deploy Virtual Machines and monitor
their basic status. The primary objective for this first sprint is to establish
the core API integration between our platform, OpenTofu, and OpenStack to enable
the instantiation of a virtual machine and return a basic status to the user.
The Management Console is primarily aimed at Developers and DevOps Engineers,
with no immediate plans for a user-friendly console for non-technical users.

**Core Functionalities:**

- **Basic VM Creation:** Capability to initiate the deployment of a virtual
  machine with a predefined, minimal configuration.

- **OpenStack API Connectivity:** Establish the necessary API connections and
  authentication with OpenStack services (primarily Nova for VM creation).

- **OpenTofu Automation for VM Deployment:** Implement the logic within our
  platform to generate a basic OpenTofu script for VM creation based on a user
  request. After that, execute the OpenTofu script to interact with OpenStack
  and then process the response from OpenTofu (success/failure) and relay it
  back to the user.

- **Dashboard:** A very basic overview, primarily focused on displaying the
  status of VM creation requests.


### Non-functional Requirements
After a lengthy discussion with the client, we outlined a series of
non-functional requirements that should be present during the project's
development phase. Among these are the following:

- **Scalability**
- **Approachability**

Scalability is a core aspect of our page, and we chose to treat it as such.
Through productive conversations with the client, we concluded that the MVP
wouldn’t need to account for a large influx of traffic at first. This, of
course, would change in the future were we to fully deploy it. Therefore, we
must ensure that both the chosen architecture and code base allow for future
scalability. Processing times must also remain impartial to a growing
population, so we must monitor how the interface handles large quantities of
incoming and outgoing traffic.

Another highly important characteristic that must be present in the proposed
solution is approachability. Through our conversations, we concluded that the
average user of a Private Cloud Interface will have basic knowledge regarding
cloud computing, VM instancing, among other cloud resources. Therefore, the
management interface won’t shy away from displaying the full functionalities of
the CloudStack cloud. On the other hand, the Cloud Administrator must have a
different view for their assigned tasks, like networking, which means that we
must alter the management interface to align with their tasks as well.


### Domain Modelling
Due to the nature of this project, we felt that a context diagram would fit best
for an overall model of the solution, as a class diagram or an ERD would not
describe our project as well as we would like to for this first sprint.
Therefore, please refer to section 1.3 if you wish to see the diagram

### Components and Subsystems
Since the proposed architecture is rather small and doesn't require many
components, we instead chose to make a comparison between a select number of
software that could be used for our solutions; and tried to discern what
benefits and setbacks they could offer us. These softwares would be used for the
private cloud creation and resource provisioning section of the architecture.
![Characterizaton](assets/sprint-0/comparison-summary.jpeg)

When it comes to the actual web interface, we have considered the use of
languages such as Python, Javascript, and even PHP and their respective
framworks for the front-end side of the equation. Additionally, a Infrastructure
as Code language is needed to accurately send infomation to CloudStack. For
this, we have considered using the language Terraform, which has been commonlly
used in conjuction to Openstack in the past. However, alternative options such
as OpenTofu are still on the table.

### Components Diagram

![Component Diagram](assets/sprint-0/rizu-component_diagram.jpg)

## Mock-ups

### Prototype

[🔗 Interactive prototype in
Figma](https://www.figma.com/proto/KDMwk1YlroBoogTSAcXtUG/rizu-prototype?node-id=2721-30&p=f&t=lwDIrgPCZDuaX6t3-1&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=2721%3A30).

<!-- omit in toc -->
#### Dashboard

![Dashboard.](assets/sprint-0/rizu-prototype-dashboard.png)

### Testing

During a meeting with the client, we presented the initial design of our
platform and showed the dashboard layout. The client approved the proposed
design and suggested using colors similar to those on Softserve’s website for
the final application, so it feels more familiar.

Additional test cases for the interactive mockup include demonstrating how the
interface looks and behaves when a user initiates the creation of a VM. While
testing this scenario, the client recommended looking into more similar
platforms to identify best practices and more features we could incorporate.
