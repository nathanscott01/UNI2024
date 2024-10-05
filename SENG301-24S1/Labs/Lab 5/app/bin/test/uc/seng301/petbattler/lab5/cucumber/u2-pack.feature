Feature: U2 As Alex, I want to create a pack so that I can build a set of pets to use in battle

  Scenario Outline: AC1 - A pack has to have a unique, non-empty alphanumeric name
    Given There is no pack with name <name>
    When I create a pack named <name> with player <player> containing pets <pets>
    Then An exception is thrown
    Examples:
    | name  | player  | pets  |
    | "pack1" |
