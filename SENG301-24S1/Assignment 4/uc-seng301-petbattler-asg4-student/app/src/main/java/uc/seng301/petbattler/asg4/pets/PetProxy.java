package uc.seng301.petbattler.asg4.pets;

import uc.seng301.petbattler.asg4.model.Pet;

/**
 * Card generation proxy for getting random card from API
 * **Note:** This proxy pattern has been identified for you, it is **not** an acceptable answer for Task 1
 * @author seng301 teaching team
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
