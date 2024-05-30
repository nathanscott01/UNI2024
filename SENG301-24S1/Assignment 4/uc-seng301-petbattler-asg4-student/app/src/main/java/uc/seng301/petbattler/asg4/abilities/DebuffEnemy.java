package uc.seng301.petbattler.asg4.abilities;

import uc.seng301.petbattler.asg4.cli.CommandLineInterface;
import uc.seng301.petbattler.asg4.model.GamePet;

/**
 * Special ability that debuffs the enemy's damage by {@link #DEBUFF_AMOUNT}
 * @author seng301 teaching team
 */
public class DebuffEnemy implements SpecialAbility {
    /**
     * Amount of debuff to apply
     */
    private static final int DEBUFF_AMOUNT = 2;

    /**
     * Debuffs other's attack by {@link #DEBUFF_AMOUNT} and prints information to cli
     * @param self current pet
     * @param other enemy pet
     * @param cli interface to print information to
     */
    @Override
    public void useSpecialAbility(GamePet self, GamePet other, CommandLineInterface cli) {
        cli.printLine(String.format("[%s debuffs %s for %d]", self.getEmoji(), other.getEmoji(), DEBUFF_AMOUNT));
        other.debuffAttack(DEBUFF_AMOUNT);
    }
}
