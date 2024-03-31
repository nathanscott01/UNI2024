package uc.seng301.petbattler.lab6.pets;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import uc.seng301.petbattler.lab6.model.Pet;

/**
 * Card
 */
public class PetResponse {
    @JsonDeserialize
    @JsonProperty("name")
    private String name;

    @JsonDeserialize
    @JsonProperty("attack")
    private int attack;

    @JsonDeserialize
    @JsonProperty("health")
    private int health;

    @JsonDeserialize
    @JsonProperty("tier")
    private int tier;

    public PetResponse() {
        // no-args jackson constructor
    }


    public Pet toPet() {
        Pet pet = new Pet();
        pet.setName(name);
        pet.setAttack(attack);
        pet.setHealth(health);
        pet.setTier(tier);
        return pet;
    }


}
