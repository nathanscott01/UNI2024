package uc.seng301.petbattler.asg4;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

/**
 * Entry class
 * @author seng301 teaching team
 */
public class App {
    private static final Logger LOGGER = LogManager.getLogger(App.class);

    /**
     * Application entry point, runs the main game loop until player quits
     *
     * @param args command line parameters
     */
    public static void main(String[] args) {
        LOGGER.info("Starting application...");
        Game game = new Game();
        game.loadDefault();
        game.play();
    }
}
