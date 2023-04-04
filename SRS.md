# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Kushal Koneni](kkoneni@uncc.edu)
* [Nicole Wiktor](nwiktor@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction

In this section, you should give a brief overview of what your project will be. Describe the software system you are building and what problems it solves. You should also give a short description of the stakeholders (users of the system) and what their needs are. There is no set formatting requirement, but you should maintain a consistent structure across future sections. Not all members must contribute to this section.
Ask what country and city you're living in and where you want to go to. It is suggest the shortest route to get to the destination

## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

* **CIRC-1:**
  * **Description:** This requirement is to store information on what country the user lives in.
  * **Type:** Functional
  * **Priority:** 3
  * **Rationale:** This requirenment is needed to know where the user hails from
  * **Testing:** This program can be tested creating a variable that will store the data of the user's country, and do a run though to see if the program

* **CIRC-2:**
  * **Description:** store the distance between airports
  * **Type:** Non-Functional
  * **Priority:** 1
  * **Rationale:** we need to know how far each airport is from one another
  * **Testing:** we shall test by storage of the variable

* **CIRC-3:**
  * **Description:** This requirenment stores info on countries the user would like to visit
  * **Type:** Non-Functional
  * **Priority:** 1
  * **Rationale:** creates a list of countries for conviniece
  * **Testing:** This will be tested when the data is stored

* **CIRC-4:**
  * **Description:** This requirement is to store information on what country the user wants to go to.
  * **Type:** Functional
  * **Priority:** 1
  * **Rationale:** This requirement is important because the only way we can tell the user the shortest route to get to their destination, we need to know where they want to go.
  * **Testing:** The requirement can be tested by creating a variable that will store the data of the user's destination, and do a run though to see if the program can track the destination required.

* **CIRC-5:**
  * **Description:** This requirement is to store information on what city the user lives in.
  * **Type:** Functional
  * **Priority:** 2
  * **Rationale:** This requirement is important because we need to know what city the user lives in in order to find out the route from their location to destination.
  * **Testing:** This program can be tested creating a variable that will store the data of the user's location, and do a run though to see if the program

* **CIRC-6:**
  * **Description:** Store information about their preferred airline
  * **Type:** Functional
  * **Priority:** 3
  * **Rationale:** This requirement is important because we need to know what plane the user wants to fly with to get to their destination.
  * **Testing:** This requirement can be tested by having a system that tracks the airlines and checks if the user's input is stored in the system.

## Constraints

In this section, you should list any constraints that you have for the project. Each group member must supply at least two constraints. These can be constraints on the project itself, the software system, or the stakeholders. Constraints can be anything that limits the scope of the project. For example, that this project's template code is written using Flask and Python constitutes a constraint on the backend of the project. Constraints can also be things like the required timeline of the project. Be creative.
Having a implossible amount of countries to travel
Having a implossible amount of airlines to travel
wether to include domestic or reginal with international
We may not be able to gauge distances precisely

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

* **TRI-1**  
  * **Description:** A user wants to find the shortest route from their current location to a specific destination in the same city.
  * **Actors:** User, routing system for the map data
  * **Preconditions:** User has a device with an internet connection and GPS capability, routing system has access to up-to-date map and traffic data.
  * **Postconditions:** User is given the shortest route to the destination, including estimated travel time and distance.

* **TRI-2**  
  * **Description:** User pays money to book a plane.
  * **Actors:** User, The person who wants to book a plane ticket and pays for it.
  * **Preconditions:** User's payment has been processed and confirmed by the system. User receives a confirmation of the booked flight with all relevant details like flight number, date, and time.
  * **Postconditions:** User's payment has been processed and confirmed by the system. User receives a confirmation of the booked flight with all relevant details like flight number, date, and time.

* **TRI-3**  
  * **Description:** User tries to see what airline is best to travel with
  * **Actors:** User, database
  * **Preconditions:** keep in mind the user's airline preference and what countries they want to visit
  * **Postconditions:** lists best airline routs and airport cites

* **TRI-4**  
  * **Description:** User wants to know the time it would take to travel to certain countries in one trip
  * **Actors:** User, database
  * **Preconditions:** the user would need to input what countries they want to go to, and their current country
  * **Postconditions:** lists the time and distance of each plane ride.

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

* **SQU-1**
  * **Type of User:** Navigator
  * **Description:** Someone who would explore different airports destinations in different countries.

* **SQU-2**
  * **Type of User:** Domestic
  * **Description:** Someone who wants to see flight options from cities within their country

* **SQU-3**
  * **Type of User:** Distance
  * **Description:** User will check the distance between different airports of their choosing

* **SQU-4**
  * **Type of User:** airline
  * **Description:** In this senario a user will look to see what flights destinations are avalible through their preffered airline

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Term:** The term that is being defined. This should be a single word or phrase that is being defined.
  * **Definition:** A definition of the term. This should be a short description of the term that is being defined. This should be a single sentence that describes the term.

* **Term:** Distance
  * **Definition:** length or time from two airports

* **Term:** airline
  * **Definition:** different airlines and the airports they are hub's of.