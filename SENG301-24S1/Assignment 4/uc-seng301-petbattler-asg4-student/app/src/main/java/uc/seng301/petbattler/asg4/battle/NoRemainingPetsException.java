package uc.seng301.petbattler.asg4.battle;

/**
 * Custom exception representing the state where a team is out of pets
 * @author seng301 teaching team
 */
public class NoRemainingPetsException extends RuntimeException {

    /**
     * Default constructor calling super {@link Exception} class
     */
    public NoRemainingPetsException() {
        super();
    }
}
