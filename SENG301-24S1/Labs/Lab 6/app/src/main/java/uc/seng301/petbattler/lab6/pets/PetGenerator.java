package uc.seng301.petbattler.lab6.pets;

import uc.seng301.petbattler.lab6.model.Pet;

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
