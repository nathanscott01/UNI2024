package uc.seng301.petbattler.asg4.model;

import uc.seng301.petbattler.asg4.abilities.AbilityCreator;
import uc.seng301.petbattler.asg4.abilities.SpecialAbility;

/**
 * Wrapper for {@link Pet} for use in battles
 * @author seng301 teaching team
 */
public class GamePet extends Pet {

    private final SpecialAbility specialAbility;


    /**
     * Create a new GamePet with a random ability
     *
     * @param name pet name
     * @param attack pet attack
     * @param health pet health
     * @param emoji emoji representation of pet
     */
    public GamePet(String name, int attack, int health, String emoji) {
        super();
        super.setName(name);
        super.setAttack(attack);
        super.setHealth(health);
        super.setEmoji(emoji);
        this.specialAbility = AbilityCreator.getRandomAbility();
    }

    /**
     * Create a new GamePet with a specified ability
     *
     * @param name pet name
     * @param attack pet attack
     * @param health pet health
     * @param emoji emoji representation of pet
     * @param specialAbility pet ability
     */
    public GamePet(String name, int attack, int health, String emoji, SpecialAbility specialAbility) {
        super();
        super.setName(name);
        super.setAttack(attack);
        super.setHealth(health);
        super.setEmoji(emoji);
        this.specialAbility = specialAbility;
    }

    /**
     * Decrease the pets current health by some amount
     *
     * @param damageAmount amount to decrease health by
     */
    public void takeDamage(int damageAmount) {
        super.setHealth(super.getHealth() - damageAmount);
    }

    /**
     * Increase the pets current health by some amount
     *
     * @param healAmount amount to increase health by
     */
    public void heal(int healAmount) {
        super.setHealth(super.getHealth() + healAmount);
    }

    /**
     * Increase the pets attack by some amount
     *
     * @param buffAmount amount to increase attack by
     */
    public void buffAttack(int buffAmount) {
        super.setAttack(super.getAttack() + buffAmount);
    }

    /**
     * Reduce the pets attack by some amount
     * May not go below 1 to avoid infinite battles
     *
     * @param debuffAmount amount to reduce attack by
     */
    public void debuffAttack(int debuffAmount) {
        super.setAttack(Math.max(1, super.getAttack() - debuffAmount));
    }

    @Override
    public boolean equals(Object o) {
        return o == this;
    }

    @Override
    public int hashCode() {
        // return the hashcode of the object's memory address since our equals() checks for same instance
        return System.identityHashCode(this);
    }

    /**
     * Makes a clone of the GamePet
     * Note: this does not deep copy the ability
     * @return clone of game pet
     */
    @Override
    public GamePet getGamePet() {
        return new GamePet(super.getName(), super.getAttack(), super.getHealth(), super.getEmoji(), specialAbility);
    }

    /**
     * setting value directly is not allowed
     * @param attack INVALID
     */
    @Override
    public void setAttack(int attack) {
        throw new UnsupportedOperationException("Can not set GamePet attack directly");
    }

    /**
     * setting value directly is not allowed
     * @param health INVALID
     */
    @Override
    public void setHealth(int health) {
        throw new UnsupportedOperationException("Can not set GamePet health directly");
    }

    /**
     * Gets printable stats string for battle with emojis
     * @return printable stats string
     */
    public String getStatsString() {
        return String.format("\uD83D\uDDE1:%d \uD83D\uDC97:%d", super.getAttack(), super.getHealth());
    }

    /**
     * Get pet ability
     * @return pets ability
     */
    public SpecialAbility getSpecialAbility() {
        return specialAbility;
    }

    /**
     * Gets printable overview string for battle with emojis
     * @return printable overview string
     */
    @Override
    public String toString() {
        return String.format("%s \t%s \uD83D\uDDE1:%d \uD83D\uDC97:%d", super.getName(), super.getEmoji(), super.getAttack(), super.getHealth());
    }
}
