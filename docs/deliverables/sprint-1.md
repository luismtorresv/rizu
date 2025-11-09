---
title: "Sprint 1: MVP Prototype"
icon: "material/view-dashboard-outline"
---

## Executive Summary

> What has been will be again,<br>
> what has been done will be done again;<br>
> there is nothing new under the sun.<br>
>
> _Ecclesiastes 1:9 (NIV)_

### Business Description

Rizu is an alternative dashboard to OpenStack's Horizon targeted at developers
with little to no cloud computing experience that want to set up a private cloud
on-premise.

### Founders/Management Team

Our team is composed of four Computer Science students with experience in web
development, cloud infrastructure deployment, computer networking, and design.

### Products and services

We only offer one product: Rizu. Besides developing the program, we offer
installation, support, and maintainance to organizations.

### Target Market

We are targeting junior developers who want to set up their own private cloud
on-premises. This includes small to medium companies that already own the
hardware needed to do a deployment of this kind, but lack the capacity to hire a
full-time expert to manage it.

### Competition

We are competing with dashboards such as Horizon (developed by the OpenStack
team) and [other similar projects](https://doi.org/10.1145/3507524.3507546).

<!----------------------------------------------------------------------------->

## Business Description

### History and background

Rizu was born from a problem in cloud computing: there wasn’t a platform that
was both affordable and easy to use. Our goal is to remove barriers that
developers and small businesses face, such as the high licensing costs on
platforms like AWS or Azure, and how complicated private cloud solutions can be.

So far, we have deployed an OpenStack installation and developed a Proof of
Concept dashboard, written in Django, that provides access to key services in
cloud computing.

### Business Mission and Vision

Our mission is to support individuals, small businesses, and educational
institutions with an intuitive, affordable, and accessible on-premise private
cloud platform, facilitating experimentation, development, and application
management, as well as exploration of learning in their own server environments.

Out vision is to become the leading on-premise private cloud platform that
enables individuals,small businesses, and educational institutions to innovate,
learn, and grow with full technological autonomy.

### Values

Accessibility and simplicity are key elements of our product. We design our
platform to be easy to use, removing complexity so users can focus on what
really matters: their projects.

### Short and Long-term Objectives

Our long-term objectives are to provide a simple and innovative dashboard that
both individual users and small companies can easily adopt.

Our short-term plans include providing services related to processing, VM
instancing, storage, and networking. These elements will be progressively rolled
out. We also want to create a user-journey of sorts, that will familiarize users
with cloud computing infrastructure.

### Business Model Canvas

![Business Model Canvas of Rizu](assets/sprint-1/rizu-bmc.jpg)

<!----------------------------------------------------------------------------->

## Market analysis

### Market Research

For Rizu’s market analysis, we focused on the private cloud computing sector.
According to Emma (2025, ["Cloud market share trends to watch in 2025"][emma]),
global cloud services are still dominated by AWS, Azure, and Google Cloud, which
together hold more than 60% of the market share. These platforms are powerful
and widely adopted, particularly by large corporations, due to their scalability
and extensive service offerings.

[emma]: <https://www.emma.ms/blog/cloud-market-share-trends>

Despite their success, these providers present challenges for smaller audiences:
- **High costs** that make these platforms less affordable for students and
  small to medium-sized enterprises.
- Although student credits are available, they are typically **limited in
  scope** and expire quickly.
- **Complex platforms** that are not always intuitive for beginners or smaller
  organizations with limited resources, and that often provide more services
  than are actually needed.

In addition, alternative cloud solutions often come with high learning curves
(e.g OpenStack) or are equally expensive (e.g VMware).

### Market segmentation

In the cloud computing market, PaaS (Platform as a Service) serves developers
and IT teams looking for agility, scalability, and ready-to-use environments.
Positioned between IaaS and SaaS, it enables rapid application development
without the complexity of infrastructure management. Rizu fits precisely here:
an on-premise private cloud PaaS that is simple and intuitive.

### Customer Base

Rizu focuses on users who value agility, simplicity, and cost-effectiveness:

- **Small to medium-sized businesses** that already own hardware and want to
  deploy a private cloud.
- **Universities** that want to provide cloud infrastructure for learning and
  research.
- **Junior developers** and **students** who need a practical, low-cost
  environment to learn and experiment.

### Competitive Analysis

We are not trying to compete with large cloud providers such as AWS or GCP, nor
with OpenStack itself. OpenStack already offers the [Horizon
dashboard][horizon]:

> Horizon is the canonical implementation of OpenStack’s Dashboard, which
> provides a web based user interface to OpenStack services including Nova,
> Swift, Keystone, etc.

[horizon]: <https://docs.openstack.org/horizon/latest/>

Horizon's comprehensive swath of panels and tabs offers customization at a cost:
high operational complexity and a steep learning curve. Instead, we offer a more
convenient way to interact with the underlying OpenStack installation.

![Horizon dashboard](assets/sprint-1/horizon.png)

<!----------------------------------------------------------------------------->

## Product/Service

### Product/Service Description

Rizu aims to provide a cost-effective, simplified PaaS that allows new
developers to dip their hands into the world of cloud networking and computing
through an on-premise deployment of a private cloud. We use the OpenStack
Ansible installation to quickly deploy its components, which can be easily
refactored by third parties for additional customization. With Rizu’s automated
creation systems, you can quickly set up a private cloud and get it ready for
your users’ needs. Such needs include VM instancing, Image storage, Volume
storage, networking, and other components that can be easily enabled during the
Ansible installation.

### Value Offer

Licensing schemes and overall complexity are issues that most newcomers to the
field struggle with. When teaching a room full of students who haven’t yet
grasped the full idea behind cloud computing, you have to get practical.
However, said practicality is quite expensive, especially with the costs
associated with operating in IaaS platforms such as AWS or Azure. Furthermore,
private cloud software, while available, isn’t intuitive enough for new
developers, and the ones that are usually come at a steep price point (looking
at you, VMware). Therefore, Rizu was made with one mentality in mind: *to offer
both a cost-effective and intuitive platform for new developers to get
accustomed to the field of cloud computing*.

With the use of the open-source, private cloud provider OpenStack, we developed
our own dashboard, which, unlike OpenStack’s Horizon, is made with up-and-coming
developers in mind. It offers a simplified version of the private cloud creation
pipeline and sets everything up behind the scenes so that administrators and
users can get into the nitty-gritty as quickly as possible. The private cloud
can also be adjusted to suit the administrator’s needs, thanks to Ansible’s
flexible configuration.

### Product Life Cycle

#### Context

Although this sprint was meant to focus on stages 4 and 5 of the software
development cycle (corresponding to Development and Testing, respectively), due
to the uncertain nature of our project's value proposition and complex
deployment, we spent most of our time debating and looking back at stages 2 and
3, which are all centered around design.

#### Currently

After multiple meetings with our client and having talked with our teacher about
our ideas, we settled on a project whose value proposition lined up with their
ideas for the course. After having spent 70-80% of this sprint on the planning
phase, we had little time to develop a working MVP, so we agreed to make some
compromises for the expected prototype. Regarding testing, thanks to the nature
of our project and of our development plans for it, we chose Scenario Testing as
our main testing method for the project, since we could check the
functionalities of every user story by checking each acceptance criteria.

#### Future

We are likely to spend the next sprint cycling through stages 2-5 of the SDLC,
planning and developing the core features of our project. We hope that going
forward, the change from stage to stage will be far smoother and less stressful
than it was this time.

<!----------------------------------------------------------------------------->

## Implementation

### Schedule

![Timeline created in Miro.](assets/sprint-1/rizu-timeline.jpg)

### Milestones

#### Current sprint

We debated quite a bit with both our client and our teacher, with the subject
being the scope of the prototype of this first sprint. In the end, we agreed to
the following milestones:

1. The Rizu dashboard must have the ability to create new projects within
OpenStack through some sort of user input. The Amount of expected inputs can
vary, but they must all lead to the creation of a new project, which must be
visible within the dashboard itself.

2. All API connections will be done using the OpenStack SDK. We must learn how
to use it first, and then we can integrate it with our project.

#### For future sprints

Lastly, we talked about what we wouldn't do for this sprint due to both time
constraints and the difficulty of the task. Although Terrafom and IaC
implementation is a critical aspect of this project, we concluded that that
particular milestone would be better suited for the 2nd sprint.

Other OpenStack projects would also be left for the second sprint, such as Nova;
although in this particular case, it was because of an infrastructure error that
we couldn't solve in time for this first sprint.

There is also the matter of the cloud deployment in the university
infrastructure, and while that space has been opened to us, we are still using
the Azure VM to test our prototype until further notice.

### Resource Requirements

#### Kolla-Ansible OpenStack Deployment

Thanks to Ansible, we gain the ability to install every single OpenStack project
at any given time. This allows for future growth if needed, and it also
simplifies the installation process by reducing the complexity of installing
each component individually.

#### Python

Python was our preferred language due to our familiarity and its ease of access
when it came to OpenStack. This is due to the already available OpenStack SDK
for Python, which allowed us to connect to the myriad APIs found in the
open-source software.

#### Django

We also chose Django due to our familiarity with it. Everybody in the team was
already familiar with it, and since we chose to use a client-server-based
architecture using MVC, Django was our go-to opinionated framework for the task.

#### Bootstrap

The mockups for our dashboard were quite detailed, and we couldn't spend too
much time thinking about the styles of each element of our application, so we
chose to use the Bootstrap classes to fill out our views and templates.

#### Python OpenStack libraries

The OpenStack SDK for Python, which came as API access for the different
projects found in OpenStack: Nova, Neutron, Keystone, etc. The OpenStack SDK
libraries grant us quick access to the cloud's systems with easy-to-understand
classes and modules.

#### Azure Virtual Machine

This resource has been critical for our development plans, since we can plan
ahead of a real deployment by using the Azure VMs to simulate what the
deployment of both our private cloud and our dashboard and project creation
page.

<!----------------------------------------------------------------------------->

## Functional Test Case Design

### Test Cases

For this project, we developed 3 major user stories that represented the main
selling points of this first sprint. Those being: Networking, project creation,
and dashboard feedback. Here are the 3 links to the respective user stories. In
the comments of said user stories are the description of each test, as well as a
video demonstrating the functionality specified in each acceptance criteria. We
chose to go for Scenario Testing due to the nature of our project.

- [Project Creation](https://github.com/luismtorresv/rizu/issues/27)
- [Networking](https://github.com/luismtorresv/rizu/issues/28)
- [Dashboard functionality and
  feedback](https://github.com/luismtorresv/rizu/issues/29)

#### Trial and Error

There weren't any apparent errors or bugs in the recordings of each test case.
However, the Django logs indicate a couple of mistakes and failed calls, which
will be appropriately marked as bugs and placed in the queue.

<img
src="https://github.com/user-attachments/assets/abcb6641-7711-4130-af4e-497458b1de09"
/>


#### UT-TC-Error Connections
<img
src="https://github.com/user-attachments/assets/221d7b45-5ff3-4916-92b4-3375e8d64314"
/>

<img
src="https://github.com/user-attachments/assets/9cf84dcd-ae64-4641-86f1-6f59971ef917"
/>

<!----------------------------------------------------------------------------->

## Software Quality

### Naming Standards

As our application is entirely written in Python, we only concern ourselves with
Python style. PEP8, a well-known standard with widespread community support, was
an initial good choice for our project.

However, we decided to go along with the Black code style which "can be viewed
as a strict subset of PEP 8" ([ref][black-code-style-section]). As the project
documentation states,

> _Black_ aims for consistency, generality, readability and reducing git diffs.

[black-code-style-section]:
    <https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#code-style>

We won't rehash those ideas here. For more information, see the [_Black_ code
style][black-code-style], the [PEP8 document][pep], or Kenneth Reitz's excellent
[stylized presentation on PEP8][pep-stylized].

[black-code-style]:
    <https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html>
[pep]: <https://peps.python.org/pep-0008/>
[pep-stylized]: <https://pep8.org/>

### Static Code Analysis

#### Linter

We use the `pylint` static code analyzer with a `max-line-length = 88` so that
it works nicely [with Black][black-pylint-line]. It is currently run manually
with the command `pylint Rizu frontPage` (the two Python modules we have so
far), as requiring it to be successful in order to merge a pull request could be
overbearing. As the [documentation][pylint-smarter] says:

> Pylint isn’t smarter than you: it may warn you about things that you have
> conscientiously done or check for some things that you don’t care about.

Does it always make sense to have a module docstring, for instance? Pylint is
highly configurable, though, and could be fitted into our preferred style and
needs. Sure, it is more opinionated and, self-admittedly, slower, but it's more
comprehensive than many other linters.

[black-pylint-line]:
    <https://black.readthedocs.io/en/stable/guides/using_black_with_other_tools.html#pylint>
[pylint-smarter]: <https://pylint.readthedocs.io/en/latest/#how-to-use-pylint>

#### Formatting Rules

To enforce the formatting rules, we set up a GitHub Action that runs `black`
("The uncompromising Python code formatter") on each push or pull request:

```yaml
name: Run Black formatter
on: [push, pull_request]
jobs:
    format:
        runs-on: ubuntu-latest
        steps:
            - name: Checkout repo
              uses: actions/checkout@v4
            - name: Run black
              uses: rickstaa/action-black@v1.3.3
              with:
                black_args: ". --check"
```

We do _not_ automatically fix formatting errors (we would need an extra GH
Action like Stefan Zweifel's popular [`git-auto-commit-action`][gaca]), but we
do block pull requests until they pass the formatting check.

[gaca]: <https://github.com/stefanzweifel/git-auto-commit-action>

### Branching Strategy

We will follow the GitHub Flow branching strategy.

Compared to Gitflow, GitHub Flow has less cognitive overhead, as `feature`
branches get merged into the `main` branch as soon as they are approved, instead
of every now and then. As for trunk-based development, we found it too simple
for a team of two that has to work on independent issues at the same time,
possibly causing merge conflicts ([Git branching strategies - AWS Prescriptive
Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/git-branching-strategies.html)).

To enforce this, we defined a GitHub branch ruleset forbidding pushes to the
`master` branch without going through a pull request first.

### Pull Requests

Additionally, the aforesaid ruleset requires that another person reviews the
code first and that all review threads are resolved. As an aside, it also blocks
merging until the GitHub action that checks whether the code is properly
formatted (i.e. that `black --check .` has a success exit code).

Here's the JSON version of the ruleset:

```json
{
  "id": 7831407,
  "name": "master",
  "target": "branch",
  "source_type": "Repository",
  "source": "luismtorresv/rizu",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "exclude": [],
      "include": [
        "~DEFAULT_BRANCH"
      ]
    }
  },
  "rules": [
    {
      "type": "deletion"
    },
    {
      "type": "non_fast_forward"
    },
    {
      "type": "creation"
    },
    {
      "type": "required_linear_history"
    },
    {
      "type": "pull_request",
      "parameters": {
        "required_approving_review_count": 1,
        "dismiss_stale_reviews_on_push": true,
        "require_code_owner_review": false,
        "require_last_push_approval": false,
        "required_review_thread_resolution": true,
        "automatic_copilot_code_review_enabled": false,
        "allowed_merge_methods": [
          "squash",
          "rebase"
        ]
      }
    }
  ],
  "bypass_actors": [
    {
      "actor_id": 5,
      "actor_type": "RepositoryRole",
      "bypass_mode": "always"
    }
  ]
}
```

### Security

1. We enabled GitHub's Dependabot alerts. This will notify us if any of our
   dependencies has a vulnerability, allowing us to quickly respond to the
   potential threat. This works. Dependabot relies on the configuration file,
   that would be `requirements.txt` in this case.

2. We enabled GitHub's secret scanning alerts. Since our project relies on API
   connections to private cloud deployments, it is essential to prevent leakage
   of secret tokens that would potentially allow an attacker to gain
   unauthorized access to our system (e.g. the upcoming deployment on EAFIT's
   premises).
