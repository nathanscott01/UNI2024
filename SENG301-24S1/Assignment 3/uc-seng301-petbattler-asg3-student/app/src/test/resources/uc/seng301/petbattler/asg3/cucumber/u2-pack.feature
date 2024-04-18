Feature: U2 As Alex I want to create a pack so that I can build a set of pets to use
  Scenario: AC1.1 - A pack has non-empty alphanumeric name
    Given I create a player named "Te Ariki"
    And Player "Te Ariki" has no packs with the name "My first pack"
    When I create the pack with name "My first pack" for "Te Ariki"
    Then The pack is created with name "My first pack" for "Te Ariki"

  Scenario Outline: AC1.2 - A pack cannot have an empty, non-alphanumeric, or numeric only name
    Given Player "Te Ariki" exists
    Then I am not allowed to create the pack with name <name> for "Te Ariki"
    Examples:
      | name     |
      | ""       |
      | ")(^$%^" |
      | "12345"  |
      | "   "    |

  Scenario: AC2 - A must pack have a unique name
    Given I create a player named "Yiyang"
    And Player "Yiyang" already has a pack with the name "My first pack"
    Then I am not allowed to create the pack with name "My first pack" for "Yiyang"

  Scenario: AC3 - A pack must be able to store many pets
    Given I create a player named "Rohan"
    When I create the pack with name "My first pack" for "Rohan"
    And I add a pet named "Kererū" with attack 7 and health 3 in pack "My first pack" for "Rohan"
    And I add a pet named "Hamster" with attack 2 and health 1 in pack "My first pack" for "Rohan"
    Then The pack "My first pack" of "Rohan" includes a pet named "Kererū"
    And The pack "My first pack" of "Rohan" includes a pet named "Hamster"