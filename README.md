# drf_nexus-cares
# NexusCARES
by {{ Mienke Dreyer }}
She Codes crowdfunding project - DRF Backend.

## About
{{ Creating an app to simplify and promote volunteers and funding for Nexus Care's projects. Nexus Care is an existing organization based in Brisbane that provides various community services, including food relief programs, career coaching clinics, emergency financial relief, and workplace English classes.This app could play a crucial role in supporting Nexus Care's efforts and expanding their impact, allowing for more community involvement in funding but also volunteers.

. }}

## Features
{{ The features your MVP will include. (Remebber this is a working document, you can change these as you go!) }}
* [Project Listings] Create a section where Nexus Care can list their ongoing and upcoming projects, such as food relief programs, career coaching clinics, emergency financial relief, and workplace English classes. Each project should have a detailed description, the expected impact, and the amount of funding or volunteers needed.
* [Volunteer Sign-Up] Offer a user-friendly interface that allows individuals to sign up as volunteers for specific projects. Volunteers can indicate their availability, skills, and interests, which will help Nexus Care match them with suitable projects.ture

### Stretch Goals
{{ Outline three features that will be your stretch goals if you finish your MVP }}

* [Donation Platform] Implement a secure payment gateway to facilitate financial contributions from users. People interested in supporting Nexus Care's projects can donate money to specific initiatives or the organization as a whole.
* [Skills Matching] Develop a feature that allows users to list their skills and expertise, and then match them with projects that require those particular skills. For example, if someone is good at marketing, they can be directed to projects that could benefit from their marketing knowledge.
* [Progress Tracking] Provide regular updates on the progress and impact of completed projects, showcasing the difference volunteers and donors have made in the community.
* [Expansion to Flash Projects] Enable a feature where Nexus Care or other organizations can post flash projects or urgent needs that require immediate attention. This can include emergency relief for individuals or families facing unforeseen circumstances.
*[Social Sharing] Encourage users to share their involvement and contributions on social media platforms, promoting the app and attracting more volunteers and donors.

## API Specification

| HTTP Method | Url | Purpose | Request Body | Successful Response Code | Authentication <br /> Authorization
| --- | ------- | ------ | ---- | -----| ----|
| GET | projects/ | Return all projects | N/A | 200 | N/A |
| POST | projects/ | Create a new project | project object | 201 | User must be logged in. |

## Database Schema
{{ Insert your database schema }}

![image info goes here](url/<src='https://dbdiagram.io/embed/64c7125502bd1c4a5ef246c7'> )

## Wireframes
{{ Insert your wireframes }}

![image info goes here](./docs/image.png)

## Colour Scheme
{{ Existing colour scheme used by Nexus Care }}

![basic diagram showing colours and codes to be used](<crowdfunding/img/colours and fonts.png>)![orange](crowdfunding/img/orange.png)![blue](crowdfunding/img/blue.png)![green](crowdfunding/img/green.png)

## Fonts
{{ Uses Hallo Euroboy and Helvetica }}![Euroboy](<crowdfunding/img/hallo Euroboy.png>)![Helvetica](<crowdfunding/img/helvetica .png>)

## Submission Documentation
{{ Fill this section out for submission }}

Deployed Project: [Deployed website](http://linkhere.com/)

### How To Run
{{ What steps to take to run this code }}

### Updated Database Schema
{{ Updated schema }}

![image info goes here](./docs/image.png)

### Updated Wireframes
{{  Updated wireframes }}

![image info goes here](./docs/image.png)

### How To Register a New User
{{ Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data). }}

### Screenshots
* [] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
![image info goes here](./docs/image.png)

* [] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
![image info goes here](./docs/image.png)

* [] A screenshot of Insomnia, demonstrating a token being returned.
![image info goes here](./docs/image.png)