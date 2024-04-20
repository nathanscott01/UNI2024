package uc.seng301.petbattler.asg3.cucumber.step_definitions;

import io.cucumber.java.BeforeAll;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.junit.jupiter.api.Assertions;
import org.mockito.Mockito;
import uc.seng301.petbattler.asg3.Game;
import uc.seng301.petbattler.asg3.accessor.PackAccessor;
import uc.seng301.petbattler.asg3.accessor.PetAccessor;
import uc.seng301.petbattler.asg3.accessor.PlayerAccessor;
import uc.seng301.petbattler.asg3.cli.CommandLineInterface;
import uc.seng301.petbattler.asg3.model.Pack;
import uc.seng301.petbattler.asg3.model.Pet;
import uc.seng301.petbattler.asg3.model.Player;
import uc.seng301.petbattler.asg3.pets.PetGenerator;
import uc.seng301.petbattler.asg3.pets.PetService;

import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;

public class BuildTeamFeature {
    private static SessionFactory sessionFactory;
    private static Game game;
    private static CommandLineInterface cli;
    private static PlayerAccessor playerAccessor;
    private static PackAccessor packAccessor;
    private static PetAccessor petAccessor;
    private static List<Pet> uniquePets;
    private static PetGenerator petGeneratorSpy;
    private static int unique_pet_i = 0;
    public static Queue<String> mockCLIResponse;

    @BeforeAll
    public static void before_or_after_all() {
        Logger.getLogger("org.hibernate").setLevel(Level.SEVERE);
        Configuration configuration = new Configuration();
        configuration.configure();
        sessionFactory = configuration.buildSessionFactory();
        playerAccessor = new PlayerAccessor(sessionFactory);
        packAccessor = new PackAccessor(sessionFactory);
        petAccessor = new PetAccessor(sessionFactory);

        uniquePets = createPredefinedPets();

        // Mockito to mock overwritten calls to API
        petGeneratorSpy = Mockito.spy(new PetService());
        Mockito.when(petGeneratorSpy.getRandomPet()).thenAnswer(i ->
                uniquePets.get(unique_pet_i)
        );

        // Mock the command line to inject user interactions
        cli = Mockito.mock(CommandLineInterface.class);
        game = new Game(petGeneratorSpy, cli, sessionFactory);

        // Use a queue to inject input into CLI
        mockCLIResponse = new LinkedList<>();
        Mockito.when(cli.getNextLine()).thenAnswer(i -> mockCLIResponse.poll());
    }

    private static List<Pet> createPredefinedPets() {
        List<Pet> pets = new ArrayList<>();
        pets.add(petAccessor.createPet("Ziggy the Corgi Cat", 2, 2, 1));
        pets.add(petAccessor.createPet("Pig", 6, 4, 1));
        pets.add(petAccessor.createPet("Donkey", 8, 6, 2));
        pets.add(petAccessor.createPet("Arabian White Horse", 8, 8, 2));
        pets.add(petAccessor.createPet("Fenton the Dog", 1, 100, 3));
        return pets;
    }

    public void assertUniquePets(Pack pack) {
        List<Pet> pets = pack.getPets();
        Set<Pet> petSet = new HashSet<>(pets);
        Assertions.assertEquals(pets.size(), petSet.size());
    }

    @Given("Player {string} has a pack {string} with {int} unique pets")
    public void player_has_a_pack_with_unique_pets(String playerName, String packName, Integer n_pets) {
        // Write code here that turns the phrase above into concrete actions
//        throw new io.cucumber.java.PendingException();

        Player player = playerAccessor.getPlayerByName(playerName);
        Pack pack = packAccessor.createPack(packName, player, new ArrayList<>());
        Long deckId = packAccessor.persistPack(pack);
        Assertions.assertNotNull(deckId);
        while (unique_pet_i < n_pets) {
            mockCLIResponse.clear();
            mockCLIResponse.add("Y");
            game.addToPack(String.format("add \"%s\" \"%s\"", playerName, pack.getName()));
            Assertions.assertTrue(
                    pack.getPets().stream().anyMatch(pet -> uniquePets.get(unique_pet_i).getName().equals(pet.getName())));
            unique_pet_i++;
        }
        unique_pet_i = 0;
        Assertions.assertEquals(n_pets, pack.getPets().size());
        assertUniquePets(pack);
    }

    @When("I, {string}, try to build a team with {string}")
    public void i_try_to_build_a_team_with(String string, String string2) {
        // Write code here that turns the phrase above into concrete actions
        throw new io.cucumber.java.PendingException();
    }

    @Then("I am informed that the pack must have at least one pet")
    public void i_am_informed_that_the_pack_must_have_at_least_one_pet() {
        // Write code here that turns the phrase above into concrete actions
        throw new io.cucumber.java.PendingException();
    }

    @When("I don't select any options")
    public void i_don_t_select_any_options() {
        // Write code here that turns the phrase above into concrete actions
        throw new io.cucumber.java.PendingException();
    }

    @Then("I am given {int} options to choose")
    public void i_am_given_options_to_choose(Integer int1) {
        // Write code here that turns the phrase above into concrete actions
        throw new io.cucumber.java.PendingException();
    }

    @When("I do not choose three pets")
    public void i_do_not_choose_three_pets() {
        // Write code here that turns the phrase above into concrete actions
        throw new io.cucumber.java.PendingException();
    }

}