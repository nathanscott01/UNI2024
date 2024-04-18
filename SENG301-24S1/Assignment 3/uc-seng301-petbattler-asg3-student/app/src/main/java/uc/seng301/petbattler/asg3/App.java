package uc.seng301.petbattler.asg3;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class App {
    private static final Logger LOGGER = LogManager.getLogger(App.class);

    /**
     * Application entry point, runs the main game loop until player quits
     * 
     * @param args command line parameters
     */
    public static void main(String[] args) {
        LOGGER.info("Starting application...");
        new Game().play();
    }
}
