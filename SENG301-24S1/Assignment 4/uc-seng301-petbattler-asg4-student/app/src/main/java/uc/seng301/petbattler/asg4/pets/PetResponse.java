package uc.seng301.petbattler.asg4.pets;

import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import uc.seng301.petbattler.asg4.model.Pet;

/**
 * Jackson mapper class for pet response from API
 * @author seng301 teaching team
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

    @JsonDeserialize
    @JsonProperty("emoji")
    private String emoji;

    /**
     * Public no-args constructor for Jackson
     */
    public PetResponse() {
        // no-args jackson constructor
    }

    /**
     * Converts the JSON representation of a pet returned by the API into a pet object
     * @return the mapped pet object made from the JSON object
     */
    public Pet toPet() {
        Pet pet = new Pet();
        pet.setName(name);
        pet.setAttack(attack);
        pet.setHealth(health);
        pet.setTier(tier);
        pet.setEmoji(emoji);
        return pet;
    }
}
