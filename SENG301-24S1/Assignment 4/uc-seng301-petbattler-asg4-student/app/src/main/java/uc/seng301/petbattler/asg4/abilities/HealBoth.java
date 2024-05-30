package uc.seng301.petbattler.asg4.abilities;

import uc.seng301.petbattler.asg4.cli.CommandLineInterface;
import uc.seng301.petbattler.asg4.model.GamePet;

/**
 * Special ability that heals both the current and enemy pet by {@link #HEAL_AMOUNT}
 * @author seng301 teaching team
 */
public class HealBoth implements SpecialAbility {
    /**
     * Amount to heal for
     */
    private static final int HEAL_AMOUNT = 2;

    /**
     * Heals self and other by {@link #HEAL_AMOUNT} and prints information to cli
     * @param self current pet
     * @param other enemy pet
     * @param cli interface to print information to
     */
    @Override
    public void useSpecialAbility(GamePet self, GamePet other, CommandLineInterface cli) {
        cli.printLine(String.format("[%s heals self for %d and heals %s for %d]", self.getEmoji(), HEAL_AMOUNT, other.getEmoji(), HEAL_AMOUNT /2));
        self.heal(HEAL_AMOUNT);
        other.heal(HEAL_AMOUNT /2);
    }
}
