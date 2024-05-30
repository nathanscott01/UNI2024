package uc.seng301.petbattler.asg4.cucumber.step_definitions;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.junit.jupiter.api.Assertions;
import org.mockito.Mockito;
import io.cucumber.java.BeforeAll;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import uc.seng301.petbattler.asg4.Game;
import uc.seng301.petbattler.asg4.accessor.PackAccessor;
import uc.seng301.petbattler.asg4.accessor.PetAccessor;
import uc.seng301.petbattler.asg4.accessor.PlayerAccessor;
import uc.seng301.petbattler.asg4.cli.CommandLineInterface;
import uc.seng301.petbattler.asg4.model.Pack;
import uc.seng301.petbattler.asg4.model.Pet;
import uc.seng301.petbattler.asg4.model.Player;
import uc.seng301.petbattler.asg4.pets.PetGenerator;
import uc.seng301.petbattler.asg4.pets.PetService;

public class AddPetFeature {
    private static SessionFactory sessionFactory;
    private static PlayerAccessor playerAccessor;
    private static PackAccessor packAccessor;
    private static PetAccessor petAccessor;
    private static PetGenerator petGeneratorSpy;
    private static CommandLineInterface cli;
    private static List<String> capturedCLIOutput;
    private static Game game;
    private static Runnable doLater;
    public static Queue<String> mockCLIResponse;
    private Pet randomPet;

    @BeforeAll
    public static void before_or_after_all() {
        Logger.getLogger("org.hibernate").setLevel(Level.SEVERE);
        Configuration configuration = new Configuration();
        configuration.configure();
        sessionFactory = configuration.buildSessionFactory();
        playerAccessor = new PlayerAccessor(sessionFactory);
        packAccessor = new PackAccessor(sessionFactory);
        petAccessor = new PetAccessor(sessionFactory);

        // set up mockito to mock overridden calls (spy) to API
        petGeneratorSpy = Mockito.spy(new PetService());
        Mockito.when(petGeneratorSpy.getRandomPet()).thenAnswer(i->
             petAccessor.createPet("Corgi", 2, 1, 1)
        );
        // mock command line, so we can inject user interactions
        cli = Mockito.mock(CommandLineInterface.class);
        game = new Game(petGeneratorSpy, cli, sessionFactory);

        // using a queue to inject input into the CLI
        mockCLIResponse = new LinkedList<>();
        Mockito.when(cli.getNextLine()).thenAnswer(i -> {
            String response = mockCLIResponse.poll();
            System.out.println("mocked input provided: " + response);
            return response;
        });

        // Capture standard out to test and for debugging purposes
        capturedCLIOutput = new ArrayList<>();
        Mockito.doAnswer((i) -> {
            capturedCLIOutput.add(i.getArgument(0));
            System.out.println((String) i.getArgument(0));
            return null;
        }).when(cli).printLine(Mockito.anyString());
    }

    // Note that the @given clause of AC1-AC4 are reusing CreateNewPackFeature methods

    // AC1,2,3,4
    @Given("Player {string} has an empty pack with the name {string}")
    public void player_has_an_empty_pack_with_the_name(String playerName, String packName) {
        Player player = playerAccessor.getPlayerByName(playerName);
        Pack pack = packAccessor.createPack(packName, player, new ArrayList<>());
        Long deckId = packAccessor.persistPack(pack);
        // we only apply the minimum checks here, as this feature has been tested elsewhere
        Assertions.assertNotNull(deckId);
        Assertions.assertTrue(pack.getPets().isEmpty());
    }

    // AC1,2,3,4
    @When("I draw a randomly selected pet")
    public void i_draw_a_randomly_selected_pet() {
        randomPet = petGeneratorSpy.getRandomPet();
        Assertions.assertNotNull(randomPet);
    }

    // AC1
    @Then("The pet has valid name, attack, health, and tier")
    public void the_pet_has_valid_name_attack_health_and_tier() {
        Assertions.assertNotNull(randomPet);
        Assertions.assertNotNull(randomPet.getName());
        Assertions.assertTrue(randomPet.getAttack() > 0);
        Assertions.assertTrue(randomPet.getHealth() > 0);
        Assertions.assertTrue(randomPet.getTier() > 0);
    }

    // AC2
    @When("I confirm I want to keep the pet in pack {string} for {string}")
    public void i_confirm_i_want_to_keep_the_pet_in_pack_for(String packName, String playerName) {
        mockCLIResponse.clear();
        mockCLIResponse.add("Y");
        doLater = () -> game.addToPack(String.format("add \"%s\" \"%s\"", playerName, packName));
        doLater.run();
    }

    // AC2
    @Then("The pet is added to the pack {string} of {string}")
    public void the_pet_is_added_to_the_pack_of(String packName, String playerName) {
        Pack pack = playerAccessor.getPlayerByName(playerName).getPacks().stream()
                .filter(p -> packName.equals(p.getName())).findFirst().orElse(null);
        Assertions.assertNotNull(pack);
        Assertions.assertTrue(
                pack.getPets().stream().anyMatch(pet -> randomPet.getName().equals(pet.getName())));
        Assertions.assertTrue(
                capturedCLIOutput.get(capturedCLIOutput.size() - 1).contains("Pet saved"));
    }

    // AC3
    @When("I confirm I do not want to keep the pet in pack {string} for {string}")
    public void i_confirm_i_do_not_want_to_keep_the_pet_in_pack_for(String packName,
            String playerName) {
        mockCLIResponse.clear();
        mockCLIResponse.add("N");
        doLater = () -> game.addToPack(String.format("add \"%s\" \"%s\"", playerName, packName));
        doLater.run();
    }

    // AC3
    @Then("The pet is not added to the pack {string} of {string}")
    public void the_pet_is_not_added_to_the_pack_of(String packName, String playerName) {
        Pack pack = playerAccessor.getPlayerByName(playerName).getPacks().stream()
                .filter(p -> packName.equals(p.getName())).findFirst().orElse(null);
        Assertions.assertNotNull(pack);
        Assertions.assertTrue(pack.getPets().stream()
                .noneMatch(pet -> randomPet.getName().equals(pet.getName())));
    }

    // AC4
    @Then("I cannot add a pet with the same name in the pack {string} of {string}")
    public void i_cannot_add_a_pet_with_the_same_name_in_the_pack_of(String packName,
            String playerName) {
        Pack pack = playerAccessor.getPlayerByName(playerName).getPacks().stream()
                .filter(p -> packName.equals(p.getName())).findFirst().orElse(null);
        Assertions.assertNotNull(pack);
        Assertions.assertTrue(
                pack.getPets().stream().anyMatch(pet -> randomPet.getName().equals(pet.getName())));
        Assertions.assertThrows(IllegalArgumentException.class, () -> pack.addPets(randomPet));
    }
}
