---
title: "Weekly: Week 10"
---

## About the meeting

- Date: 2025-09-20
- Time: 14:58-15:21
- Participants: Jerónimo Acosta, Juan Sebastián Jácome, Paula Llanos, Luis Torres
- Recording: [Link to SharePoint][recording]

[recording]: <https://eafit.sharepoint.com/:v:/s/Rizu/EdYmvYxvhVVHu8_QodTuSJ4BnNrhfWDAhBPzAnAI2Jdr8Q?e=gOf84z>

!!! note "AI-generated content disclaimer"

    The following is an AI-generated summary of the meeting based on the
    transcript.

## progress on authentication system and openstack integration

* **jeronimo** updated the team, including **luis miguel**, on advancements in
  user authentication with different roles and discussed pending integration of
  openstack user creation, the location of the code changes, and the pull
  request process.

* **status of authentication:** jeronimo explained that role-based
  authentication is already implemented in the system, but the creation of an
  openstack user upon creating a rizu user is still pending.
* **location and change management:** luis miguel asked about the location of
  the changes, and jeronimo clarified they are on a branch called
  *auth-and-new-front-application*, while discussing whether to open a pull
  request before completing integration.
* **pull request process:** luis miguel suggested opening a draft pull request
  so progress is visible to the team, noting that review notifications are
  only sent once a formal review is requested.

## task updates and weekly progress

* **luis miguel, paula, juan sebastian,** and **jeronimo** shared their weekly
  progress, including work on the project selector, dashboard styling, cv
  updates, and user story assignments.

* **individual contributions:** paula fixed the project selector and applied
  new dashboard styling in css, building on jeronimo’s branch. juan sebastian
  reported dedicating time to updating his cv for a job application.
* **user story assignment and review:** luis miguel and jeronimo reviewed user
  story assignments to ensure all members have tasks and clarified issues
  around their visibility in the platform.
* **github workflow:** luis miguel emphasized committing changes to the main
  branch and notifying him for review to maintain clear and controlled
  progress tracking.

## sprint 2 documentation and deliverables

* **luis miguel** and **paula** reviewed sprint 2 documentation, covering fixed
  and variable costs, projections, and pending marketing and sales strategy, as
  well as wiki automation.

* **documentation status:** paula confirmed inclusion of cost tables and
  projection spreadsheets, while final polishing and upload of the document
  remain pending.
* **marketing and sales:** luis miguel highlighted that the marketing and
  sales strategy still needs to be completed, expecting either next class or
  usability test sessions to address it.

## usability testing and automated tests

* **luis miguel** and **jeronimo** differentiated between usability tests and
  automated tests, opting to focus on functional tests and considering code
  coverage.

* **usability tests:** luis miguel explained usability testing as observing
  users’ interactions with the system to collect feedback on their experience.
* **functional testing:** the team agreed that with no complex algorithms,
  simple functional automated tests are more appropriate than advanced setups
  like selenium for scenario testing.

## academic datacenter (dca) access and network setup

* **luis miguel** informed the team about issues with access to the university’s
  dca, use of private ips, vpn requirements, and the lack of clear guidance from
  professor edwin montoya.

* **access conditions:** luis miguel explained that the team’s ip address is
  private within the dca, requiring vpn access instead of direct internet
  connections.
* **communication with professor:** luis miguel and jeronimo agreed to use
  monday’s distributed systems project presentation to request the guide from
  professor edwin, acknowledging they may need to follow up persistently.

## daily reports and code formatting tools

* **luis miguel** discussed daily reports and code formatting tools. jeronimo
  experienced issues with black configuration for pre-commit formatting, and
  luis suggested using vs code’s auto format on save.

* **daily reports:** luis miguel confirmed he will continue sharing daily
  updates in the whatsapp group, though noting that on days with little
  progress, there may be no report.

## delivery planning and work organization

* **luis miguel** and **jeronimo** reviewed upcoming deadlines, absence of
  meetings with **leon**, and the importance of steady progress to avoid
  workload buildup during recess week.

* **delivery deadlines:** the team confirmed october 15 as the next delivery
  date and noted there will be no meeting with leon this week, leaving more
  time for task progress.
* **work organization:** luis miguel and jeronimo agreed to advance on tasks
  whenever possible to avoid last-minute pressure during october recess.

# follow-up tasks

* **jeronimo**: complete the integration so that creating a user in rizu also
  creates one in openstack.
* **jeronimo**: open a pull request from the branch
  *auth-and-new-front-application* and request review when ready.
* **paula**: finalize and upload sprint 2 document including fixed/variable
  costs and projections.
* **team**: add the marketing and sales strategy section to the sprint 2
  document.
* **luis miguel**: verify and ensure all user stories are correctly assigned in
  github.
* **team**: request the dca access guide from professor edwin montoya.
