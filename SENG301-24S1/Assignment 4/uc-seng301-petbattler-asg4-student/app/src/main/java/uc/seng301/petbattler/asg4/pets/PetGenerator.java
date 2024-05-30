package uc.seng301.petbattler.asg4.pets;

import uc.seng301.petbattler.asg4.model.Pet;

/**
 * Card generation interface
 * @author seng301 teaching team
 */
public interface PetGenerator {
    /**
     * Get a random card
     * @return a randomly generated card
     */
    Pet getRandomPet();
}
