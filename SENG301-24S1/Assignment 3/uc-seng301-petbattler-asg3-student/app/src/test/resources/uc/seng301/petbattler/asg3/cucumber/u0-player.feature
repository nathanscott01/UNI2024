Feature: U0 As Alex, I want to create a Player so that I can use it to play Super Auto Pets.

  Scenario Outline: AC1 - A player cannot contain non-alphanumeric or numeric-only values.
    Given There is no player with name <name>
    Then I am not allowed to create a player with name <name>
    Examples:
      | name    |
      | "72363" |
      | "-"     |
      | "-&%#@" |
      | " "     |
