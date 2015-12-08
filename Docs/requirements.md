#Hoppa Requierement Specifications
##1. Introduction
###1.1. Purpose
The purpose of this document is to provide a description of the system requirements for Hoppa web application. The requirements described in this document are to provide a complete picture of the requirements to implement this system. 
###1.2. Document Conventions
The following acronyms, abbreviations or terms with definitions used in this document. 

##Term/Acronym Definition
GUI: Graphical User Interface

##1.3. Intended Audience and Reading Suggestions
This document is intended to be used by the ICOM5016 DataBase Systems course students - Keysha M. González Colón, Rolando C. Ortiz Santiago and Yanisse M. Rodríguez Torres - as a guideline for the design and implementation of the Hoppa web application. Also, to be used by the Teaching Assistant - David Bartolomei, and the ICOM5016 DataBase Systems course professors - Kejie Lu and Bienvenido Velez - to evaluate the software requirement definitions for the system.
##1.4. Product Scope
This document describes the system functionality required to allow college students to access a social network where they will be able to provide and receive assistance with courses they are struggling with, creating or joining Study Groups where they can solve exercises, post unanswered exercises for assistance, etc. These groups can be created for any topic, such as math, science, history, among others. Though not exclusively usable by only students, students are the intended audience and the network will be based around their use. This service will connect students in order to help them provide mutual aid. Through this service, students will have a more personal support when searching for help with homework, study exercises, group study meetings and the like. It will also allow students to corroborate the solutions found by communicating with their peers directly and being able to leave a review of how well they like a given solution. Based on these reviews and how many problems they help solve, users will be given a certain rank. All users start out as an Egg and by helping others move up through the ranks of Tadpole, Tadpole with Legs, Tailed Frog, Adult Frog, and Elder Frog.
Hoppa will not support video or voice chat. It will also be a web app and is currently not planned to have mobile support in its first version.
When faced with a troublesome problem, most students will turn to the internet or their friends for help. Unfortunately, they may not always find the solution online, or they may find but not understand it. Furthermore, they may not have a means by which to contact all their friends, or they may not feel comfortable asking some of them for help out of the blue. Hoppa will solve both of these problems. While not guaranteeing a solution to your problem, it will allow you to obtain help from any Hoppa friend willing to come to your aid, or your fellow group members. If someone manages to solve your problem and you don’t understand the solution, you need only ask them to clarify.
##1.5. References
Not applicable. 
##1.6. Overview
General Description
External Interface Requirements
Functional Requirements
Non Functional Requirements 
##2. General Description
###2.1. Product Perspective
The product is, as of right now, entirely independent and is intended to provide a method for students to learn even when they are unable to get in contact with their professors, instructors, or even their friends. Hoppa improves this aspect by giving easier access to this software from a personal computer. This web application is not going to have interfaces with other applications. 
###2.2. System Evolution and Product Functions
The product will have a GUI that is accessible from laptop/desktop web browser.
It will have two main interfaces, one for standard users to create study groups and events, give/receive assistance inside the groups, sell or buy books, and the second one for expert users to provide tutoring services. 
The product will store user profiles information, groups, posts, events and services inside an SQL server that will serve as the backbone for the entire software.
The user can initiate a study group or can join other student users discussions. 
Users can rate posts from one to five, and the author of the post or answers will receive ranking points; the rank will vary between Egg, Tadpole, Tadpole with Legs, Tailed Frog, Adult Frog, and Elder Frog.
The user can create study group sections or tutoring sections as events and invite other students.
The user will receive notifications via email. Notifications can include an email when a new response to a post is received, when another user joins a group, notifications for upcoming events, when another user follows them, when another user gives feedback about the user’s assistance, when another user posts in a group, among others. 
The product will also provide expert users a GUI to manage services such as sell books, provide tutoring services, and create learning and tutoring events. 
The user requires basic knowledge on computer and internet browsing.
The is not software installation required to use the Hoppa. It will be accessible via web services provided by any computer web browser.
###2.3. Users Classes and Characteristics
There are three types of user classes in this product:
*Standard Users: The students that can create study groups, post exercises and problems, create events and assist other students.
*Expert Users: The expert user is an extension to the standard user. The main difference is that the expert does not needs to be a student, it could be professors, instructors or businesses such as tutoring institutions, that can provide tutoring services. If a standard user ranks between Adult Frog and Elder Frog, it can have the same privileges as an expert user.
*Site-Admin: The site admin has the authority of adding and removing user accounts. It is the one that is in charge of curate relevant content to reach the Hoppa’s ideal customers. Also, creates, curates, and manages all published content (images and written). Develops and expands community. Monitors, listens and respond to users in a “Social” way and oversees design.
###2.4. Operating Environment
The main operating environment will be a web interface. It will be used for personal laptop/desktop environment. As described above in this document’s Scope section, Hoppa will not be available for mobile environments. 
###2.5. Design and Implementation Constraints
Hoppa development is limited under AngularJS, Java Play and MySQL frameworks.
###2.6. User Documentation
Documentation will be provided for each phase on the course of the project. It will cover what we believed to be the requirements needed for the project and also some non essential requirements as well. We will have the source code documented as well along with a manual that describes all the features and interfaces that we implement. Hoppa will require a help section to assist users.
###2.7. Assumptions and Dependencies 
We are assuming that this project may be used by college students and tutors around the world so we are designing it to be a user friendly social network under the ICOM5016 DataBase Systems and our frameworks’ standards. The team depends on software IDE and MySQL management software since we plan to use a SQL server as the backbone for this project. Regarding data requirements, more information is needed to determine the category of the products or services that we will provide in the database. 
##3. External Interface Requirements
###3.1. User Interface 
The primary user interface will be a Web-enabled tool developed to allow users to create and join study groups in order to get assistance from other users from the same or similar college courses. 
###3.2. Hardware Interface
The Web-enabled tool will be accessed through web browsers, the user can access it from laptops and desktops. 
###3.3. Software Interface 
The system will utilize a web application running on Play Framework along with Angular JS scripting as the backend, data will be held in a SQL database. Users are allowed to create a Hoppa account using an email address as username and a password, the user will authenticate using the email address and the password. Users will initiate the application going to an URL and can interact with the system using a standard web browser.
##4. System Features and Functional Requirements
###4.1. Create Account
####4.1.1. Description
In order to access the website and its services, the user must have an account. To create an account, the user must provide an email address, a password, their name, their place of study, their major. There will be three major account types: standard, expert, and administrator. The standard account is for ordinary users and will be the most common one. The expert user will be the account meant for tutors and other teaching services. When creating the account, they will be able to choose whether or not they are an “expert” user. These accounts can advertise their help services and help in groups if they wish. Finally, administrators are able to modify the web page. This login will be restricted to only the three members of the group working on the project for now.
####4.1.2. Response Sequence
The site will inform the user whether or not their account was created successfully. If successfully created, the site will load the user’s home page.
####4.1.3. Functional Requirements
REQ-1: The system provides informs the user whether or not their account was created successfully.
##4.2. Login
####4.2.1. Description
If the user already has an account on the site, they can log into it to access the its services. In order to log into the website, the user must have created an account prior to this and is required to input an email account and its corresponding password. There will be at least three different forms of login. One is the general user login which will allow the user to access the website’s standard services.
####4.2.2 Response Sequence
If the user’s email and password are correct, the site will display the user’s home page. Upon entering an incorrect username or password, the user will be informed that one of the two was incorrect.
####4.2.3. Functional Requirements
REQ-2: The system provides means for the user to input the following login information: email, password.
REQ-3: If the user submits an incorrect set of credentials, the system will let them know their email or password is incorrect.

###4.3. Create Group
####4.3.1. Description
A user is able to create a study group with other users in order to share information on the course and help each other with course exercises. In order to create a group, the user will be prompted with what name they wish to give it, which category it will be filed under, what users they would like to make into members of the group, and whether or not the group will be private. At this time, the creator will be set as the group’s administrator.
####4.3.2 Response Sequence
The user will be notified whether or not their group has been successfully created. If it is successfully created, the site will display the newly created group page.
####4.3.3. Functional Requirements
REQ-4: The system will provide the user with a means to submit the following information: group name, category, administrator.
###4.4. Create Event
####4.4.1. Description
Users will also be able to create events. These are meant to organize meetings, get togethers, and tutoring sessions. The user will be asked to input the event’s time and place, and give a short description of the event.
####4.4.2 Response Sequence
The user will be notified whether or not their event was successfully created. If successfully created, the site will display the newly created event page.
####4.4.3. Functional Requirements
REQ-5: The system will provide the user with a means to submit the following information: date, location, description.
##5. Non Functional Requirements
###5.1. Performance Requirements
###5.2. Security Requirements
The user will log into the system using an email and a personalized password. The password will require at least one lower-case letter, one capital letter, one number, and have a length of at least seven symbols.
###5.3. Software Quality Attributes
####5.3.1 Availability
The system must allow access to the user always (24/7). 
####5.3.2. Adaptability
Any web browser and database design must provide easy adaptation to changes in Hoppa support and services.
####5.3.3. Usability
The system will provide interface be suitable for all users. Upon initial user access, the system must provide a new user account form. 
###5.4. Business Rules
There are three types of user accounts defined in the functional requirements. These accounts define the operating principles of the system. Users should be assigned account types according to their role in the Hoppa environment. 

