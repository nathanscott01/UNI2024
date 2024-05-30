package uc.seng301.petbattler.asg4.battle;

import uc.seng301.petbattler.asg4.model.GamePet;

import java.util.List;

/**
 * Simple Team wrapper for a list of {@link GamePet}s and name
 * @author seng301 teaching team
 */
public interface Team extends List<GamePet> {
    /**
     * Get team name
     * @return team name
     */
    String getName();

    /**
     * Gets an in-order TeamOrdering of the team's pets
     * @return ordered pets
     */
    TeamOrdering getOrderedTeam();

    /**
     * Gets a reverse-order TeamOrdering of the team's pets
     * @return reverse-ordered pets
     */
    TeamOrdering getReversedTeam();
}
