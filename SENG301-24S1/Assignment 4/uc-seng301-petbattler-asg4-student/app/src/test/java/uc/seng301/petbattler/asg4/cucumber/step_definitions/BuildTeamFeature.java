package uc.seng301.petbattler.asg4.cucumber.step_definitions;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.function.Supplier;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.stream.IntStream;
import java.util.stream.Stream;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.junit.jupiter.api.Assertions;
import org.mockito.Mockito;
import org.mockito.stubbing.Answer;
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

public class BuildTeamFeature {

    private static PlayerAccessor playerAccessor;
    private static PackAccessor packAccessor;
    private static PetAccessor petAccessor;
    private static PetGenerator petGeneratorSpy;
    public static int petIncrement = 0;

    private static List<String> output;
    private static Game game;
    private static Runnable doLater;
    public static Queue<String> mockedInputQueue;

    @BeforeAll
    public static void before_or_after_all() {
        Logger.getLogger("org.hibernate").setLevel(Level.SEVERE);
        Configuration configuration = new Configuration();
        configuration.configure();
        SessionFactory sessionFactory = configuration.buildSessionFactory();
        playerAccessor = new PlayerAccessor(sessionFactory);
        packAccessor = new PackAccessor(sessionFactory);
        petAccessor = new PetAccessor(sessionFactory);

        // set up mockito to mock overridden calls (spy) to API
        petGeneratorSpy = Mockito.spy(new PetService());
        mockPets();

        // mock command line, so we can inject user interactions
        CommandLineInterface cli = Mockito.mock(CommandLineInterface.class);
        game = new Game(petGeneratorSpy, cli, sessionFactory);

        mockedInputQueue = new LinkedList<>();
        Mockito.when(cli.getNextLine()).thenAnswer(i -> {
            String response = mockedInputQueue.poll();
            System.out.println("mocked input provided: " + response);
            return response;
        });

        // Capture standard out to test and for debugging purposes
        output = new ArrayList<>();
        Mockito.doAnswer((i) -> {
            output.add(i.getArgument(0));
            System.out.println((String) i.getArgument(0));
            return null;
        }).when(cli).printLine(Mockito.anyString());
    }

    private void addInputMocking(String... mockedInputs) {
        mockedInputQueue.clear();
        mockedInputQueue.addAll(List.of(mockedInputs));
    }

    private static void mockPets() {
        List<Supplier<Pet>> mockedPets = new ArrayList<>();
        // mocking infinite pets (5 different bases)
        mockedPets.add(() -> petAccessor.createPet("Corgi" + petIncrement++, 2, 1, 1));
        mockedPets.add(() -> petAccessor.createPet("Ant" + petIncrement++, 2, 2, 1));
        mockedPets.add(() -> petAccessor.createPet("Badger" + petIncrement++, 2, 3, 2));
        mockedPets.add(() -> petAccessor.createPet("Cat" + petIncrement++, 4, 2, 3));
        mockedPets.add(() -> petAccessor.createPet("Lion" + petIncrement++, 5, 5, 4));
        Mockito.doAnswer(
                (Answer<Pet>) invocation -> mockedPets.get(petIncrement % mockedPets.size()).get())
                .when(petGeneratorSpy).getRandomPet();
    }

    @Given("Player {string} has a pack {string} with {int} unique pets")
    public void player_has_a_pack_with_unique_pets(String playerName, String packName,
            Integer numberOfPets) {
        Player player = playerAccessor.getPlayerByName(playerName);
        Pack pack = packAccessor.createPack(packName, player, new ArrayList<>());
        IntStream.range(0, numberOfPets).forEach(i -> {
            Pet p = petGeneratorSpy.getRandomPet();
            p.setPetId(petAccessor.persistPet(p));
            pack.addPets(p);
        });
        Long deckId = packAccessor.persistPack(pack);
        Assertions.assertNotNull(deckId);
        Assertions.assertEquals(pack.getPets().size(), numberOfPets);
    }

    @When("I, {string}, try to build a team with {string} named {string}")
    public void i_try_to_build_a_team_with_named(String playerName, String packName,
            String teamName) {
        doLater = () -> game.buildTeam(
                String.format("build_team \"%s\" \"%s\" \"%s\"", playerName, packName, teamName));
    }

    @Then("I am informed that the pack must have at least one pet")
    public void i_am_informed_that_the_pack_must_have_at_least_one_pet() {
        doLater.run();
        Assertions.assertTrue(output.get(output.size() - 1)
                .contains("Cannot build team with a pack with 0 pets"));
    }

    @When("I don't select any options")
    public void i_don_t_select_any_options() {
        addInputMocking("!q");
        doLater.run();
    }

    @Then("I am given {int} options to choose")
    public void i_am_given_options_to_choose(Integer numberOfOptions) {
        IntStream.range(0, numberOfOptions).forEach(i -> Assertions.assertTrue(
                output.get(output.size() - 1 - (4 - i)).contains(String.format("[%d]", i))));
    }

    @When("I do not choose three pets")
    public void i_do_not_choose_three_pets() {
        addInputMocking("2 0", "!q");
        doLater.run();
    }

    @Then("I am informed I must choose three pets")
    public void i_am_informed_i_must_choose_three_pets() {
        Assertions.assertTrue(
                output.get(output.size() - 1).contains("Must enter 3 pets space separated"));
    }

    @When("I choose three duplicate pets")
    public void i_choose_three_duplicate_pets() {
        addInputMocking("0 0 0", "!q");
        doLater.run();
    }

    @Then("I am informed I must choose unique pets")
    public void i_am_informed_i_must_choose_unique_pets() {
        Assertions
                .assertTrue(output.get(output.size() - 1).contains("Must enter 3 unique options"));
    }

    @When("I choose pets {int}, {int}, {int}")
    public void i_choose_pets(Integer pet1, Integer pet2, Integer pet3) {
        addInputMocking(String.format("%d %d %d", pet1, pet2, pet3));
        doLater.run();
    }

    @Then("The team created has pets ordered the correct way {int}, {int}, {int}")
    public void the_team_created_has_pets_ordered_the_correct_way(Integer petIn1, Integer petIn2,
            Integer petIn3) {
        List<Integer> petReferences = List.of(petIn1, petIn2, petIn3);
        IntStream.range(0, petReferences.size()).forEach(i -> Assertions
                // make sure that the name and ID are the same as the ones selected previously, by
                // looking up into the output stack
                .assertTrue(output.get(output.size() - (5 + 4 - petReferences.get(i)))
                        .contains(output.get(output.size() - (3 - i)).split(",")[0])));
    }

    @Then("Each pet in my team is a discrete clone")
    public void each_pet_in_my_team_is_a_discrete_clone() {
        String teamPet1 = output.get(output.size() - 3);
        String teamPet2 = output.get(output.size() - 2);
        String teamPet3 = output.get(output.size() - 1);
        List<String> petReferences =
                Stream.of(teamPet1, teamPet2, teamPet3).map(s -> s.split(":")[1].strip()).toList();
        Assertions.assertEquals(petReferences.stream().distinct().count(), petReferences.size());
    }

}
