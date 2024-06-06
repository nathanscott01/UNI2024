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

The prototype pattern is used to clone a Pet object in order to create a replica of the original object as a new GamePet
object. The Pet object needs to be cloned so that an extra attribute can be added to it, called specialAbility. Cloning
the Pet object eliminates the potential overhead cost of obtaining a new pet from an external server using an API, and
makes the whole process of creating a GamePet much simpler by simply cloning it. Cloning the Pet object to create a
GamePet preserves the original instance of the Pet, allowing it to be used again in the future.

#### Name of UML Class diagram attached

./diagrams/clone-pet.png

#### Mapping to GoF pattern elements

| GoF element         | Code element                                     |
|---------------------|--------------------------------------------------|
| Prototype Interface | CloneablePet Interface                           |
| Concrete Prototype  | Pet Class                                        |
| Client              | buildTeam(String input) method within Game class |

### Pattern 2

#### What pattern is it?

Factory

#### What is its goal in the code?

*The Factory pattern is used to encapsulate the process of creating an object within a separate method. In this case, 
the GamePet object allocates the responsibility of creating the SpecialAbility object to the AbilityCreator class. This 
separates the instantiation process of the SpecialAbility object from the GamePet object, adhering to the single 
responsibility principle. The GamePet object has no need to be involved with the instantiation process, only the 
implementation of the SpecialAbility itself, so the logical approach would be to seperate it. With a factory pattern, 
the client (GamePet) is only interested in receiving the SpecialAbility, not creating it.

#### Name of UML Class diagram attached

./diagrams/special-ability-factory.png

#### Mapping to GoF pattern elements

| GoF element       | Code element                                                    |
|-------------------|-----------------------------------------------------------------|
| Factory Interface | AbilityCreator Class                                            |
| Product Interface | SpecialAbility Interface                                        |
| Concrete Products | HealSelf, BuffSelf, HealBoth, DebuffEnemy                       |
| Client            | GamePet, it uses AbilityCreator to assign SpecialAbility object |

### Pattern 3

#### What pattern is it?

Command

#### What is its goal in the code?

Within the Petbattler Game, the user wants to perform an action, in this case adding a pet to a pack. The command 
pattern is followed to handle requests such as these by seperating the invoker from the reciever, and using a command 
interface to process the request. In the case of wanting to add a pet to a pack, the Game Class is the invoker, and it 
uses the Command Line Interface (cli.getNextLine()) to represent the request as a String object. The request to add a 
pet to pack is represented as a String object, and the Concrete Command used is addToPack(String input). This Concrete 
Command performs the actions required to add a pet to a pack on a Pack object, the receiver.

#### Name of UML Class diagram attached

./diagrams/add-to-pet-command.png

#### Mapping to GoF pattern elements

| GoF element      | Code element                               |
|------------------|--------------------------------------------|
| Command          | Command Line Interface - cli.getNextLine() |
| Concrete Command | addToPack(String input)                    |
| Invoker          | Game Class                                 |
| Reciever         | Pack object                                |

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
