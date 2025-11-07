---
title: "Sprint 3: Final Product"
icon: "material/bee"
---

> “Major Major had been born too late and too mediocre. Some men are born
> mediocre, some men achieve mediocrity, and some men have mediocrity thrust
> upon them. With Major Major it had been all three. Even among men lacking all
> distinction he inevitably stood out as a man lacking more distinction than all
> the rest, and people who met him were always impressed by how unimpressive he
> was.”
>
> —Joseph Heller, _Catch-22_

## In a nutshell

During this sprint we:

* Improved the aesthetics of the user interface
* Added block storage capabilities (think AWS EBS)
* Deployed the application (almost) using a Dockerfile
* Wrote a user manual to help onboard new users
* Conducted usability tests to determine UX quality
* Simplified the overall project setup workflow

!!! question "Where's the rest of the business plan?"

    We decided to merge those sections related to the business plan from last
    sprint and the new ones in a new document called [Business Plan](business-plan.md).

<!----------------------------------------------------------------------------->

## Usability Tests Results

> “The most common user action on a Web site is to flee.”
>
> –Edward Tufte, Information Design Guru

### Context

Our UI/UX leader ~~forcibly~~ recruited four (4) fellow students to complete the
tests outlined during the previous sprint.[^1]

[^1]: I also recruited a friend to help us out with this but we, eh… had
    _technical issues_ during the test and so we removed this outlier data
    point.

Most of them, young software engineers with little to no experience with cloud
service provider consoles, were able to complete core tasks successfully[^2] and
some even praised the interface for being "modern and clear" (in Spanish).

[^2]: I mean, obviously.

### Problems

They did have some issues with:

* What the "role" is supposed to mean

* The location of the "select a project" dropdown menu

* Navigation through the interface

* Terminology related to cloud services (e.g. "What's a flavor?")

### Metrics

Here are some summary metrics you can take home:

<div class="grid cards" markdown>

- :material-clock-outline: **Average total time:** roughly 9 minutes
- :material-check: **Success rate:** 95%
- :material-alert-circle-outline: **Errors:** 1.6 per user
- :material-star: **Satisfaction rate:** 4.2/5.0

</div>

### Conclusions

We concluded that, while our current user interface is good enough for a
hypothetical user of the platform, we could enhance it by working on:

1. Clarifying what each role does. Perhaps by adding a short explanatory text
   during the sign up flow.

2. Moving the project selector to the top left corner so it's more visible. Or
   making it stand out more.

3. Adding breadcrumb navigation so users can find their way around the site or
   improving on the sidebar's design.

4. Explaining concepts such as flavors in the forms themselves instead of
   expecting the user to have read the manual.[^3]

[^3]: RTFM. Short for "Read The Fine Manual".

## User Manual

> “_[reading from the manual]_ The instructions to fit in, have everybody like
> you, and always be happy!”
>
> —Emmet Brickowoski, _The LEGO® Movie_

## Application Deployment

> “Live, from New York, it's Saturday Night!”
