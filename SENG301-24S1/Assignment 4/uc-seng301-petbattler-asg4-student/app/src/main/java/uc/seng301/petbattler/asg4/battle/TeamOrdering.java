package uc.seng301.petbattler.asg4.battle;

import uc.seng301.petbattler.asg4.model.GamePet;

/**
 * An interface to get the pets of a team in order
 * @author seng301 teaching team
 */
public interface TeamOrdering {
    /**
     * Get the next pet in order
     * @return the next available pet in the team
     * @throws NoRemainingPetsException if no more pets exist
     */
    GamePet getNextPet() throws NoRemainingPetsException;

    /**
     * Returns true iff the team has remaining pets
     * @return true iff the team has remaining pets else false
     */
    boolean hasRemainingPets();
}
