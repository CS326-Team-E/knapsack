# Overview
Our application adheres to our project proposal. It is a platform designed to
give students access to modular applications intended to improve their campus
experience. We have yet to encounter any features that are too difficult to
implement but we have prioritised certain features over others. For example,
knapsack configuration has yet to be implemented although we are confident that
we will achieve this feature soon. 

# Team Members

* Jingshu Meng
* Zhihan Ying
* Conan Chen
* William He
* Jacob Goldman

# Video Link

# Design Overview
Our application centers around three core models: Users, Knapsacks, and Tools. A
user has one knapsack which has many tools. An additional feature is Tool
Request, each of which have votes. Users, knapsacks, and tools are mapped
together under /library where we see a view of a user's knapsack and the
tools it contains. Additionally, we see a view of tools available to the user
physically represented on a map of the campus at /map. An interface to request
tools exposes tool requests and the votes for each request at /request. Lastly,
our welcome page has a logic for displaying different information based on user
authentication, although registration is not yet implemented.

# Problems/Successes
- Problems 
  * Getting different components to work together (ex. Dropdown
  nav only worked on one page)
  * Making use of the time available instead of cramming towards due date
  * Learning Django's templating language
  * Coordinating a singular vision of the finished product

- Successes
  * Great implementation of the data model: extensible and well designed
  * Once we mastered templating, we effectively created the views we needed
  * Good communication when together

