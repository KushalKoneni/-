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
#Ask what country and city you're living in and where you want to go to.
#It is suggest the shortest route to get to the destination

## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

* **CIRC-1:**
  * **Description:** 
  * **Type:** 
  * **Priority:** 
  * **Rationale:** 
  * **Testing:** 

* **CIRC-2:**
  * **Description:** 
  * **Type:** 
  * **Priority:** 
  * **Rationale:** 
  * **Testing:** 

* **CIRC-3:**
  * **Description:** 
  * **Type:** 
  * **Priority:** 
  * **Rationale:** 
  * **Testing:** 

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

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

* **TRI-1** A unique identifier for the use case. This should be a number that is unique across the entire document (something like UC-1, UC-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A description of the use case that gives the user a high-level overview of how the system is interacted with.
  * **Actors:** A list of the actors that are involved in the use case. Only include the actors that are directly involved. Actors are the people or things that interact with the system. For example, when ordering at a fast food restaurant, one might have the following actors: the customer, the cashier, and the cook. But only the customer and the cashier are directly involved in the use case of ordering food. The cook is not directly involved in the use case of ordering food.
  * **Preconditions:** A list of the preconditions for the use case. This should be a list of the preconditions for the use case, which are the conditions that must be met before the use case can be executed. Continuing with the restaurant example, the customer must have money in their wallet and the cashier must be logged in to the system before the use case of ordering food can be executed.
  * **Postconditions:** A list of the postconditions for the use case. This should be a list of the postconditions for the use case, which are the conditions that must be met after the use case has been executed. Continuing with the restaurant example, the customer must have their food and the cashier must have the customer's money after the use case of ordering food has been executed.

* **TRI-1** 
  * **Description:** 
  * **Actors:** 
  * **Preconditions:** 
  * **Postconditions:** 

* **TRI-2** 
  * **Description:** 
  * **Actors:** 
  * **Preconditions:** 
  * **Postconditions:** 

* **TRI-3** 
  * **Description:** 
  * **Actors:** 
  * **Preconditions:** 
  * **Postconditions:** 

* **TRI-4** 
  * **Description:** 
  * **Actors:** 
  * **Preconditions:** 
  * **Postconditions:** 

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

* **SQU-1** A unique identifier for the user story. This should be a number that is unique across the entire document (something like US-1, US-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Type of User:** The type of user that the user story is for. This should be a single word that describes the type of user. For example, a user story for a customer might be `Customer` and a user story for an administrator might be `Admin`.
  * **Description:** A description of the user story that gives a narrative from that user's perspective. This can be any length, but it must paint the picture of what the user wants to do, how they intend to do it, why they want to, and what they expect to happen.

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
  * **Definition:** 
