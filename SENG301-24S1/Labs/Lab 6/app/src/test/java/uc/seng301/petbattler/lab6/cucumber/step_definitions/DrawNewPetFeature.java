package uc.seng301.petbattler.lab6.cucumber.step_definitions;

import io.cucumber.java.BeforeAll;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.junit.jupiter.api.Assertions;
import org.mockito.Mockito;
import uc.seng301.petbattler.lab6.Game;
import uc.seng301.petbattler.lab6.accessor.PackAccessor;
import uc.seng301.petbattler.lab6.accessor.PetAccessor;
import uc.seng301.petbattler.lab6.accessor.PlayerAccessor;
import uc.seng301.petbattler.lab6.cli.CommandLineInterface;
import uc.seng301.petbattler.lab6.model.Pack;
import uc.seng301.petbattler.lab6.model.Pet;
import uc.seng301.petbattler.lab6.model.Player;
import uc.seng301.petbattler.lab6.pets.PetGenerator;
import uc.seng301.petbattler.lab6.pets.PetService;

import java.util.ArrayList;
import java.util.logging.Level;


public class DrawNewPetFeature {
    private static PetGenerator petGeneratorSpy;
    private static PetAccessor petAccessor;
    private static PackAccessor packAccessor;
    private static PlayerAccessor playerAccessor;
    private static Pet randomPet;
    private static CommandLineInterface cli;
    private static Game game;

    @BeforeAll
    public static void before_or_after_all() {

        java.util.logging.Logger.getLogger("org.hibernate").setLevel(Level.SEVERE);
        Configuration configuration = new Configuration();
        configuration.configure();
        SessionFactory sessionFactory = configuration.buildSessionFactory();
        packAccessor = new PackAccessor(sessionFactory);
        playerAccessor = new PlayerAccessor(sessionFactory);
        petAccessor = new PetAccessor(sessionFactory);

        petGeneratorSpy = Mockito.spy(new PetService());
        Pet mockedPet = petAccessor.createPet("Corgy", 2, 1, 1);
        Mockito.doReturn(mockedPet).when(petGeneratorSpy).getRandomPet();

        cli = Mockito.mock(CommandLineInterface.class);
        game = new Game(petGeneratorSpy, cli, sessionFactory);
    }

    @Given("Player {string} has an empty pack with the name {string}")
    public void player_has_an_empty_pack_with_the_name(String playerName, String packName) {
        Player player = playerAccessor.getPlayerByName(playerName);
        Pack pack = packAccessor.createPack(packName, player, new ArrayList<>());
        Long id = packAccessor.persistPack(pack);
        Assertions.assertNotNull(packAccessor.getPackById(id));
    }

    @When("I draw a randomly selected pet")
    public void i_draw_a_randomly_selected_pet() {
        randomPet = petGeneratorSpy.getRandomPet();
        Assertions.assertNotNull(randomPet);
    }

    @When("I confirm I want to keep the pet in pack {string} for {string}")
    public void i_confirm_i_want_to_jeep_the_pet_in_pack_for(String packName, String playerName) {
        Mockito.when(cli.getNextLine()).thenReturn("Y");
        game.addToPack(String.format("add \"%s\" \"%s\"", playerName, packName));
    }

    @When("I confirm I do not want to keep the pet in pack {string} of {string}")
    public void i_confirm_i_do_not_want_to_keep_the_pet_in_pack_of(String packName, String playerName) {
        Mockito.when(cli.getNextLine()).thenReturn("N");
        game.addToPack(String.format("add \"%s\" \"%s\"", playerName, packName));
    }

    //Unsure
    @Then("The pet has a valid name, attack, health and tier")
    public void the_pet_has_a_valid_name_attack_health_and_tier() {
        Assertions.assertNotNull(randomPet.getName());
        Assertions.assertTrue(randomPet.getAttack() > 0);
        Assertions.assertTrue(randomPet.getHealth() >= 0);
    }

    //Unsure
    @Then("The pet is added to the pack {string} of {string}")
    public void the_pet_is_added_to_the_pack_of(String packName, String playerName) {
        Player player = playerAccessor.getPlayerByName(playerName);
        Pack pack = player.getPacks().stream().filter(p -> packName.equals(p.getName())).findFirst().get();
        Assertions.assertNotNull(pack);
        Assertions.assertTrue(pack.getPets().stream().anyMatch(pet -> randomPet.getName().equals(pet.getName())));
    }

    //Unsure
    @Then("The pet is not added to the pack {string} of {string}")
    public void the_pet_is_not_added_to_the_pack_of(String packName, String playerName) {
        Player player = playerAccessor.getPlayerByName(playerName);
        Pack pack = player.getPacks().stream().filter(p -> packName.equals(p.getName())).findFirst().get();
        Assertions.assertNotNull(pack);
        String petName = randomPet.getName();
        Assertions.assertFalse(pack.getPets().stream().anyMatch(pet -> petName.equals(pet.getName())));
    }

    @Then("I cannot add a pet with the same name in the pack {string} of {string}")
    public void i_cannot_add_a_pet_with_the_same_name_in_the_pack_of(String packName, String playerName) {
        Pack pack = playerAccessor.getPlayerByName(playerName).getPacks().stream().filter(p -> packName.equals(p.getName())).findFirst().get();
        Assertions.assertNotNull(pack);
        Assertions.assertTrue(pack.getPets().stream().anyMatch(pet -> randomPet.getName().equals(pet.getName())));
        Assertions.assertThrows(IllegalArgumentException.class, () -> pack.addPets(randomPet));
    }
}
