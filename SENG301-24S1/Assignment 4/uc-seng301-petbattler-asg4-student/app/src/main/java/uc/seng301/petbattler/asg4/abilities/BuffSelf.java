package uc.seng301.petbattler.asg4.abilities;

import uc.seng301.petbattler.asg4.cli.CommandLineInterface;
import uc.seng301.petbattler.asg4.model.GamePet;

/**
 * Special ability that buffs the current pets damage by {@link #BUFF_AMOUNT}
 * @author seng301 teaching team
 */
public class BuffSelf implements SpecialAbility {
    /**
     * Amount of buff to apply
     */
    private static final int BUFF_AMOUNT = 2;

    /**
     * Buffs self's attack by {@link #BUFF_AMOUNT} and prints information to cli
     * @param self current pet
     * @param other enemy pet
     * @param cli interface to print information to
     */
    @Override
    public void useSpecialAbility(GamePet self, GamePet other, CommandLineInterface cli) {
        cli.printLine(String.format("[%s buffs self for %d]", self.getEmoji(), BUFF_AMOUNT));
        self.buffAttack(BUFF_AMOUNT);
    }
}
