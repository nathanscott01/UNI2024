package uc.seng301.petbattler.asg4.battle;

import uc.seng301.petbattler.asg4.model.GamePet;

/**
 * A helper class for in-order accessing of pets in a team
 * @author seng301 teaching team
 */
public class OrderedTeam implements TeamOrdering {
    private int currentIndex;
    private final Team pets;

    /**
     * Create a new in-order ordering of the pets within the given team
     * @param pets team to create in-order ordering of pets for
     */
    public OrderedTeam(Team pets) {
        this.pets = pets;
        this.currentIndex = 0;
    }

    @Override
    public GamePet getNextPet() throws NoRemainingPetsException {
        while (currentIndex < pets.size()) {
            if (pets.get(currentIndex).getHealth() > 0 )
                return pets.get(currentIndex++);
            currentIndex++;
        }
        throw new NoRemainingPetsException();
    }

    @Override
    public boolean hasRemainingPets() {
        while (currentIndex < pets.size()) {
            if (pets.get(currentIndex).getHealth() > 0 )
                return true;
            currentIndex++;
        }
        return false;
    }

}
