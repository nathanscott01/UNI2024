package uc.seng301.petbattler.asg4.cucumber.step_definitions;

import java.util.logging.Level;
import java.util.logging.Logger;

import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.junit.jupiter.api.Assertions;

import io.cucumber.java.BeforeAll;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import uc.seng301.petbattler.asg4.accessor.PlayerAccessor;

public class CreatePlayer {
    private static PlayerAccessor playerAccessor;

    @BeforeAll
    public static void before_or_after_all() {
        Logger.getLogger("org.hibernate").setLevel(Level.SEVERE);
        Configuration configuration = new Configuration();
        configuration.configure();
        SessionFactory sessionFactory = configuration.buildSessionFactory();
        playerAccessor = new PlayerAccessor(sessionFactory);
    }

    @Given("There is no player with name {string}")
    public void there_is_no_player_with_name(String playerName) {
        Assertions.assertNull(playerAccessor.getPlayerByName(playerName));
    }

    @Then("I am not allowed to create a player with name {string}")
    public void i_am_not_allowed_to_create_a_player_with_name(String playerName) {
        Assertions.assertThrows(IllegalArgumentException.class, () -> playerAccessor.createPlayer(playerName));
    }
}
