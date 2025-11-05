---
title: "Weekly: Week 15"
---

## About the meeting

- Date: 2025-11-01
- Time: 15:00 – 15:30
- Participants: Jerónimo Acosta, Juan Sebastián Jácome, Luis Torres
- Recording: [Link to SharePoint][recording]

[recording]: <https://eafit.sharepoint.com/:v:/s/Rizu/EVgFwWreOQVFrbnTEbnUY0IB3icIm7ZxFeiNDfOmst3zWg?e=3BDmXD>

## Notes

### Pre-meeting

- Paula won't be joining us today.

### Progress

- Luis presented the wiki sections he added on project risks and the conclusion
  of the business plan.

- Jerónimo activated the Zun service on the DCA deployment.

### Problems

- Jerónimo warned us that the university VPN server is down. Thus, we cannot
  connect to the virtual machine hosting the OpenStack deployment.

- Jerónimo described a problem where the kolla-ansible deployment created fresh
  images when deploying, which caused a decrease in disk space because of the
  unused storage. It was around 100 gigabytes and was reduced to 50 gigabytes.
  The solution is to run the deployment command using tags.

    Jerónimo mentioned how running reconfigure doesn't create new containers, so
  one has to re-deploy. That's why he had to deploy it.

- Juan Sebastián mentioned how he's been having problems working on his assigned
  tasks as he's busy with other coursework.

- Jerónimo played back the audios sent by the professor on the integration tests
  for the previous sprint.

### Follow-up tasks

- Jerónimo will start writing the user manual in a Google Docs document. He will
  give us edit access to the document. He will report on its status either **today
  or tomorrow**. Jerónimo will give step-by-step guides on the different features
  a typical user can take. He will write the document in English.

- Luis will split the sprint 3 and sprint 2 documents so that a separate
  business plan encompasses all sections related to it. He will do this **today**
  and will share the update with the team on the WhatsApp group.

- Juan Sebastián will set up the `.clouds.yaml` on his local development
  environment to iterate faster on his task of automatically setting up the
  network for the user. He will start working on this **tomorrow**.

- Luis will ask a friend of his and Jerónimo's to take part in the usability
  tests for this sprint **today**. He will report back to the team **either today or
  tomorrow**, depending on the response time.

- Luis will deploy the application **no later than Tuesday** using, most likely, a
  Docker container running gunicorn and nginx. He will keep the team posted on
  this.
