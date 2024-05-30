package uc.seng301.petbattler.asg4.battle;

import uc.seng301.petbattler.asg4.model.GamePet;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * An implementation of the Team interface that inherits from {@link ArrayList} to store GamePets without generics
 * @author seng301 teaching team
 */
public class TeamList extends ArrayList<GamePet> implements Team {
    private final String name;

    /**
     * Create a new team with a given list of pets
     * @param name name for team
     * @param pets list of pets that belong to team
     */
    public TeamList (String name, List<GamePet> pets) {
        this.name = name;
        this.addAll(pets.stream().map(GamePet::getGamePet).collect(Collectors.toCollection(ArrayList::new)));
    }

    /**
     * Create a deep-copy of a team from an existing team
     * @param other team to deep-copy
     */
    public TeamList (Team other) {
        this.name = other.getName();
        this.addAll(other.stream().map(GamePet::getGamePet).collect(Collectors.toCollection(ArrayList::new)));
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public TeamOrdering getOrderedTeam() {
        return new OrderedTeam(this);
    }

    @Override
    public TeamOrdering getReversedTeam() {
        return new ReversedTeam(this);
    }

}
