# SENG301 Assignment 4 (2024) - Student answers

** NATHAN SCOTT **

## Task 1 - Identify the patterns in the code

### EXAMPLE PATTERN (this pattern is given as an example)

#### What pattern is it?

Proxy

#### What is its goal in the code?

This proxy pattern is used in the Super Auto Pets app to:

- obtain pets from an external system (SAP API), i.e. access control to pets supplied by API;
- create cards on demand, pruning what is not needed from the retrieved cards before passing them.

#### Name of UML Class diagram attached

./diagrams/sap-proxy-domain.png

Note that the association in the UML diagram contains a composition instead of an aggregation (as in the refactoring guru) or a directed association (in the reference card). You have to represent the pattern in its implemented form, i.e. as it is in the code, to get the full marks.

#### Mapping to GoF pattern elements

| GoF element | Code element        |
| ----------- | ------------------- |
| Client      | Game                |
| Subject     | PetGenerator        |
| Proxy       | PetProxy            |
| RealSubject | PetService          |
| request()   | getRandomPet()      |

### Pattern 1

#### What pattern is it?

Prototype

#### What is its goal in the code?

**YOUR ANSWER**

#### Name of UML Class diagram attached

**YOUR ANSWER**

#### Mapping to GoF pattern elements

| GoF element | Code element |
| ----------- | ------------ |
|             |              |

### Pattern 2

#### What pattern is it?

**YOUR ANSWER**

#### What is its goal in the code?

**YOUR ANSWER**

#### Name of UML Class diagram attached

**YOUR ANSWER**

#### Mapping to GoF pattern elements

| GoF element | Code element |
| ----------- | ------------ |
|             |              |

### Pattern 3

#### What pattern is it?

**YOUR ANSWER**

#### What is its goal in the code?

**YOUR ANSWER**

#### Name of UML Class diagram attached

**YOUR ANSWER**

#### Mapping to GoF pattern elements

| GoF element | Code element |
| ----------- | ------------ |
|             |              |

## Task 2 - Full UML Class diagram

### Name of file of full UML Class diagram attached

**YOUR ANSWER**

## Task 3 - Implement new feature

### What pattern fulfils the need for the feature?

**YOUR ANSWER**

### What is its goal and why is it needed here?

**YOUR ANSWER**

### Name of UML Class diagram attached

**YOUR ANSWER**

### Mapping to GoF pattern elements

| GoF element | Code element |
| ----------- | ------------ |
|             |              |

## Task 4 - BONUS - Acceptance tests for Task 4

### Feature file (Cucumber Scenarios)

**NAME OF FEATURE FILE**

### Java class implementing the acceptance tests

**NAME OF JAVA FILE**
