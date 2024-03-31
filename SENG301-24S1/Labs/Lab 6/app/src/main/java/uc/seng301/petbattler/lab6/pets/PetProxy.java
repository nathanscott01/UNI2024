package uc.seng301.petbattler.lab6.pets;

import uc.seng301.petbattler.lab6.model.Pet;

/**
 * Card generation proxy for getting random card from API
 */
public class PetProxy implements PetGenerator {
    private final PetService petService;

    /**
     * Create a new Card proxy using the {@link PetService} implementation
     */
    public PetProxy() {
        this.petService = new PetService();
    }

    @Override
    public Pet getRandomPet() {
        return petService.getRandomPet();
    }
}
