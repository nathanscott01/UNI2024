Feature: U1 As Alex, I want to create a Pet so that I can use it in a pack.

  Scenario: AC1 - A pet has a unique non-empty name, a strictly positive attack, and positive health stats.
    Given There is no pet with name "Ant"
    When I create a pet named "Ant" with attack: 2 and health: 2
    Then The pet is created with the correct name, attack and health
    