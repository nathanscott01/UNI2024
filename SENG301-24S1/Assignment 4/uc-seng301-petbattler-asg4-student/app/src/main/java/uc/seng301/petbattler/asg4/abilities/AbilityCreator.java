package uc.seng301.petbattler.asg4.abilities;

import uc.seng301.petbattler.asg4.model.GamePet;

import java.util.Random;

/**
 * Simple helper class to pick {@link GamePet} {@link SpecialAbility}s at random
 * @author seng301 teaching team
 */
public class AbilityCreator {
    private static final Random random = new Random();

    /**
     * Static class, no public constructor
     */
    private AbilityCreator(){}

    /**
     * Get one 4 abilities randomly, options are:
     * {@link HealSelf}
     * {@link BuffSelf}
     * {@link HealBoth}
     * {@link DebuffEnemy}
     *
     * @return randomly chosen ability
     */
    public static SpecialAbility getRandomAbility() {
        int randomValue = random.nextInt(0,4);
        SpecialAbility specialAbility;
        switch (randomValue){
            case 0 -> specialAbility = new HealSelf();
            case 1 -> specialAbility = new BuffSelf();
            case 2 -> specialAbility = new HealBoth();
            default -> specialAbility = new DebuffEnemy();
        }
        return specialAbility;
    }
}
