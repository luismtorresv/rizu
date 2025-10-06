---
title: "Weekly: Week 4"
---

## About the meeting

|              |                                                                                                                                                                                                                                                                                                                        |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Date         | 2025-08-09                                                                                                                                                                                                                                                                                                             |
| Time         | 15:00-16:00                                                                                                                                                                                                                                                                                                            |
| Participants | <ol><li>Jerónimo Acosta</li><li>Juan Sebastián Jácome</li><li>Paula Llanos</li><li>Luis Torres</li></ol>                                                                                                                                                                                                               |
| Recording    | <https://eafit-my.sharepoint.com/:v:/g/personal/lmtorresv_eafit_edu_co/EX4zdKNCuCpHnw0m4x8Qs-UBOvlRs8LDT_5Wp8ykR7da6g?e=wd0dTU&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D> |

## Meeting notes

We have some questions for our upcoming meeting with the client:

1. Juan Sebastián: Regarding Terraform, JS thought the licensing changes of
   Terraform implied that it would not be used in this development.

2. Jerónimo: We want to know whether they want us to code a GUI that lets
   developers handle resources or take in Terraform scripts that are passed on
   to OpenStack, using an SDK, or maybe both or even none of them.

3. Luis: Do they have any suggestions regarding our presentation for the Design
   Sprint?

After we talked with the professor on Wednesday, we realised we had to rethink
our idea. Jerónimo and I (Luis) brainstormed a new idea: we'll develop a Django
app that is essentially a dashboard for students and people who are not
familiar with cloud computing providers that allows them to manage  a private
cloud with a simple interface. Behind the scenes we'll generate Terraform
scripts that instantiate machines.

Jerónimo is looking at an alternative way to connect with OpenStack using some
configuration that allows us to connect.

Luis will initialise the repo with the Django app.

Jerónimo proposes a client-server architecture where the server contains all the
OpenStack services. The dashboard would connect to the server that has the
OpenStack services.

Separate physical instances for the web server and the OpenStack server.

Doing a perfunctory review of the professor's feedback:

1. The installation of the PaaS has to be simple:

2. The admin must be able to manage permissions for the users:

3. The admin must be able to add or change hardware without much trouble:

4. Use Terraform to create the virtual cloud:

5. Writing our own mini-language that transpiles to Terraform?


One of the big challenges here

<https://developer.hashicorp.com/terraform/tutorials>



## Individual report

### Jerónimo Acosta
1. What did you do last week?

* I spent a good chunk of last week working on the documentation of the project. Although rushed, the team and I managed to finish every single requirement set by the Sprint 0 document on time for the Wednesday presentation. That went well, too, and we managed to compile some interesting comments from both our client and our teacher.

2. What will you do this week?

* After the weekly scheduled meeting with our client, I plan to invest some time into investigating the architecture of OpenStack, as well as how Architecture as Code software like Terraform interacts with the platform.

3. Is there an obstacle?

* Yes. There is a significant amount of academic work that prevents me from fully dedicating myself to this project. I have to figure out a way to research these topics without it interfering with the rest of my work.

### Juan Sebastián Jácome
1. What did you do last week?

    [answer here]

2. What will you do this week?

    [answer here]

3. Is there an obstacle?

    [answer here]

### Paula Llanos
1. What did you do last week?

    [answer here]

2. What will you do this week?

    [answer here]

3. Is there an obstacle?

    [answer here]

### Luis Torres
1. What did you do last week?

    I set up the wiki, wrote the problem and solution sections, scheduled the
    recurrent meetings with the client.

2. What will you do this week?

    Look into how OpenStack and Terraform work.

3. Is there an obstacle?

    We need to talk to the client to pin down some details regarding the
    implementation of our program.
