package uc.seng301.petbattler.asg4.abilities;

import uc.seng301.petbattler.asg4.cli.CommandLineInterface;
import uc.seng301.petbattler.asg4.model.GamePet;

/**
 * Pet special ability interface
 * @author seng301 teaching team
 *
 */
public interface SpecialAbility {

    /**
     * Use special ability
     * @param self current pet
     * @param other enemy pet
     * @param cli interface to print information to
     */
    void useSpecialAbility(GamePet self, GamePet other, CommandLineInterface cli);
}
