---
title: "Functional Tests"
icon: "material/screwdriver"
---

> if it ain't broke, don't fix it

## Functional Tests

We modeled Sprint  1 validation around scenario testing so every walkthrough
mimicked an end-to-end journey (networking, project rooms, dashboard feedback).

## Test Cases

- [Project Creation](https://github.com/luismtorresv/rizu/issues/27): Verified
  form validation, role gating, and confirmation cues via narrated screencast.

- [Networking](https://github.com/luismtorresv/rizu/issues/28): Recordings show
  expected topology updates.

- [Dashboard functionality and feedback](https://github.com/luismtorresv/rizu/issues/29): Focused on
   notifications, project filters, and the “join/create” loop; every acceptance
   item matched the captured video evidence.

All three stories cleared their acceptance criteria without reruns.

## Trial and Error

Manual runs looked clean, yet Django logs exposed a handful of failed POST
retries from earlier API probes. We flagged those bugs so they do not regress
into bigger errors.

## Personal Opinion

The process felt disciplined: pairing scenario scripts with recordings kept the
team accountable, and reviewing them as a group surfaced nuanced UX notes we
later folded into usability sessions. Manual verification may be slower than
automation, but for this sprint it let us judge the product’s polish and confirm
that what “works on stage” also holds up in day-to-day usage.
