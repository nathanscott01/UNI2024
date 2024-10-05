Feature: U3 As Alex, I want to draw random pets from an external API so that I can build a pack from them
  Scenario: AC1 - I can draw a random pet that has valid name, attack, health, and tier
    Given I create a player named "George"
    And Player "George" has an empty pack with the name "My first pack"
    When I draw a randomly selected pet
    Then The pet has valid name, attack, health, and tier

  Scenario: AC2 - If I find a suitable pet, I can add the pet to my pack
    Given I create a player named "Maia"
    And Player "Maia" has an empty pack with the name "My first pack"
    When I draw a randomly selected pet
    And I confirm I want to keep the pet in pack "My first pack" for "Maia"
    Then The pet is added to the pack "My first pack" of "Maia"

  Scenario: AC3 - I can decide to ignore a pet and not add it to my pack
    Given I create a player named "Li"
    And Player "Li" has an empty pack with the name "My first pack"
    When I draw a randomly selected pet
    And I confirm I do not want to keep the pet in pack "My first pack" for "Li"
    Then The pet is not added to the pack "My first pack" of "Li"

  Scenario: AC4 - A pack cannot contain twice the same pet
    Given I create a player named "Alya"
    And Player "Alya" has an empty pack with the name "My first pack"
    When I draw a randomly selected pet
    And I confirm I want to keep the pet in pack "My first pack" for "Alya"
    Then I cannot add a pet with the same name in the pack "My first pack" of "Alya"
