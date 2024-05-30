package uc.seng301.petbattler.asg4.model;

/**
 * Simple interface for defining creation of {@link GamePet}s
 * @author seng301 teaching team
 */
public interface CloneablePet {
    /**
     * Returns a distinct game pet
     * @return a distinct game pet
     */
    GamePet getGamePet();
}
