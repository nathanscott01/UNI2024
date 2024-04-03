Feature: U4 As Alex, I want to create a Team from the pets in one of my packs so that I can use it in a battle.

  Scenario: AC1 - A pack must contain at least one pet to build a team with
    Given I create a player named "Monica Bing-Geller"
    And Player "Monica Bing-Geller" has an empty pack with the name "My Empty Pack"
    When I, "Monica Bing-Geller", try to build a team with "My Empty Pack"
    Then I am informed that the pack must have at least one pet

  Scenario: AC2 - When building a team there will be 5 options randomly selected from my pack
    Given I create a player named "Ross"
    And Player "Ross" has a pack "My 5 Pet Pack" with 5 unique pets
    When I, "Ross", try to build a team with "My 5 Pet Pack"
    And I don't select any options
    Then I am given 5 options to choose

  Scenario: AC3 - When building a team I must select 3 options
    Given I create a player named "Rachel"
    And Player "Rachel" has a pack "My 5 Pet Pack" with 5 unique pets
    When I, "Rachel", try to build a team with "My 5 Pet Pack"
    And I do not choose three pets
    Then I am informed I must choose three pets

