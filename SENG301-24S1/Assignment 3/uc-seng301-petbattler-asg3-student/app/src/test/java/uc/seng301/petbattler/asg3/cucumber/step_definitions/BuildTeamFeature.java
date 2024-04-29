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
    public static Queue<String> mockCLIResponse;
    private static List<String> capturedCLIOutput;
    private static Runnable doLater;
//    private Player player;
//    private Pack pack;

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
                // create a new mocked pet each time since an instance of a pet can only exist in one pack at a time
                petAccessor.createPet("Corgy", 2, 1, 1)
        );

        // Mock the command line to inject user interactions
        cli = Mockito.mock(CommandLineInterface.class);
        game = new Game(petGeneratorSpy, cli, sessionFactory);

        // using a queue to inject input into the CLI
        mockCLIResponse = new LinkedList<>();
        Mockito.when(cli.getNextLine()).thenAnswer(i -> {
            String response = mockCLIResponse.poll();
            System.out.println("mocked input provided: " + response);
            return response;
        });

        // Capture the standard output for testing
        capturedCLIOutput = new ArrayList<>();
        Mockito.doAnswer((i) -> {
            capturedCLIOutput.add(i.getArgument(0));
            System.out.println((String) i.getArgument(0));
            return null;
        }).when(cli).printLine(Mockito.anyString());
    }

    private static List<Pet> createPredefinedPets() {
        List<Pet> pets = new ArrayList<>();
        pets.add(petAccessor.createPet("Ziggy the Corgi Cat", 2, 2, 1));
        pets.add(petAccessor.createPet("Pig", 6, 4, 1));
        pets.add(petAccessor.createPet("Donkey", 8, 6, 2));
        pets.add(petAccessor.createPet("Arabian White Horse", 8, 8, 2));
        pets.add(petAccessor.createPet("Fenton the Dog", 1, 100, 3));
        for (Pet pet : pets) {
            petAccessor.persistPet(pet);
        }
        return pets;
    }


    public void assertUniquePets(Pack pack) {
        List<Pet> pets = pack.getPets();
        Set<Pet> petSet = new HashSet<>(pets);
        Assertions.assertEquals(pets.size(), petSet.size());
    }

    @Given("Player {string} has a pack {string} with {int} unique pets")
    public void player_has_a_pack_with_unique_pets(String playerName, String packName, Integer n_pets) {
        Player player = playerAccessor.getPlayerByName(playerName);
        List<Pet> petsToAdd = new ArrayList<>(uniquePets.subList(0, n_pets));
        Pack pack = packAccessor.createPack(packName, player, petsToAdd);
        Long deckId = packAccessor.persistPack(pack);
        Assertions.assertNotNull(deckId);
        Assertions.assertEquals(n_pets, pack.getPets().size());
        assertUniquePets(pack); // Asserts all pets within set are equal
    }

    @When("I, {string}, try to build a team with {string}")
    public void i_try_to_build_a_team_with(String playerName, String packName) {
//        Pack pack = playerAccessor.getPlayerByName(playerName).getPacks().stream()
//                .filter(p -> packName.equals(p.getName())).findFirst().get();
        Player player = playerAccessor.getPlayerByName(playerName);
        Pack pack = player.getPacks().stream().filter(p -> packName.equals(p.getName())).findFirst().get();
        Assertions.assertNotNull(pack);
        doLater = () -> game.buildTeam(String.format("build_team \"%s\" \"%s\"", playerName, packName));

        // Do I add more tests here????
    }

    @Then("I am informed that the pack must have at least one pet")
    public void i_am_informed_that_the_pack_must_have_at_least_one_pet() {
        doLater.run();
        Assertions.assertTrue(capturedCLIOutput.get(capturedCLIOutput.size() - 1)
                .contains("Cannot build team with a pack with 0 pets"));
    }

    @When("I don't select any options")
    public void i_don_t_select_any_options() {
        mockCLIResponse.clear();
        mockCLIResponse.add("!q");

        // The pets shown here are not the pets I chose or simulated API
    }

    @Then("I am given {int} options to choose")
    public void i_am_given_options_to_choose(Integer int1) {
        doLater.run();
        // Count the number of lines that match the expected option format
        long count = capturedCLIOutput.stream()
                .filter(line -> line.matches("\\[\\d+\\] .*")) // Regex to match lines like [0] Option Name
                .count();
        // Assert that the number of options is as expected
        Assertions.assertEquals(int1.intValue(), count, "The number of options given does not match the expected count.");
    }

    @When("I do not choose three pets")
    public void i_do_not_choose_three_pets() {
        mockCLIResponse.clear();
        mockCLIResponse.add("1 2");
        mockCLIResponse.add("!q");
    }

    @Then("I am informed I must choose three pets")
    public void i_am_informed_i_must_choose_three_pets() {
        doLater.run();
        Assertions.assertTrue(capturedCLIOutput.get(capturedCLIOutput.size() - 1)
                .contains("Must enter 3 pets space separated"));
    }

}