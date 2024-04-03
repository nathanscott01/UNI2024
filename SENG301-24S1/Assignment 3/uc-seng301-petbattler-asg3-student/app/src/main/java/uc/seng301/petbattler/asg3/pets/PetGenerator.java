package uc.seng301.petbattler.asg3.pets;

import uc.seng301.petbattler.asg3.model.Pet;

/**
 * Card generation interface
 */
public interface PetGenerator {
    /**
     * Get a random card
     * @return a randomly generated card
     */
    Pet getRandomPet();
}
