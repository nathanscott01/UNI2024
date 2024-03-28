Feature: U1 as Alec, I want to create a Pet so that I can use it in a pack.

  Scenario: AC1 - A pet has a unique non-empty name, a strictly positive attack, and positive health stats.
    Given There is no pet with name "Ant"
    When I create a pet named "Ant" with attack: 2 and health: 2
    Then The pet is created with the correct name, attack and health

    Scenario Outline: AC2 - A pet name cannot contain non-alphanumeric or numeric-only values.
      Given There is no pet with name <name>
      When I create an invalid pet named <name> with attack: 2 and health: 2
      Then An exception is thrown
      Examples:
        | name      |
        | "673975"  |
        | "$*&ynsl" |

    Scenario Outline: AC3 - A pet has a strictly positive attack, and a positive health.
      Given There is no pet with name <name>
      When I create an invalid pet named <name> with attack: <attack> and health: <health>
      Then An exception is thrown
      Examples:
        | name    | attack | health |
        | "harry" | 2      | -1     |
        | "mick"  | -1     | 2      |
        | "zoe"   | 0      | 2      |
