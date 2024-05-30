package uc.seng301.petbattler.asg4.battle;

import uc.seng301.petbattler.asg4.model.GamePet;

/**
 * A helper class for reverse-order accessing of pets in a team
 * @author seng301 teaching team
 */
public class ReversedTeam implements TeamOrdering {
    private int currentIndex;
    private final Team pets;

    /**
     * Create a new reverse-order ordering of the pets within the given team
     * @param pets team to create reverse-order ordering of pets for
     */
    public ReversedTeam(Team pets) {
        this.pets = pets;
        this.currentIndex = this.pets.size()-1;
    }

    @Override
    public GamePet getNextPet() throws NoRemainingPetsException {
        while (currentIndex >= 0) {
            if (pets.get(currentIndex).getHealth() > 0 )
                return pets.get(currentIndex--);
            currentIndex--;
        }
        throw new NoRemainingPetsException();
    }

    @Override
    public boolean hasRemainingPets() {
        while (currentIndex >= 0) {
            if (pets.get(currentIndex).getHealth() > 0 )
                return true;
            currentIndex--;
        }
        return false;
    }

}
