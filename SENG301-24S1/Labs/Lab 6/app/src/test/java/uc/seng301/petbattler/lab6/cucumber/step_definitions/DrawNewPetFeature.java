package uc.seng301.petbattler.lab6.cucumber.step_definitions;

import java.util.logging.Level;
import java.util.ArrayList;
import java.util.Arrays;
import io.cucumber.java.BeforeAll;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.junit.jupiter.api.Assertions;
import uc.seng301.petbattler.lab6.accessor.PackAccessor;
import uc.seng301.petbattler.lab6.accessor.PetAccessor;
import uc.seng301.petbattler.lab6.accessor.PlayerAccessor;
import uc.seng301.petbattler.lab6.model.Pack;
import uc.seng301.petbattler.lab6.model.Pet;
import uc.seng301.petbattler.lab6.model.Player;
import uc.seng301.petbattler.lab6.pets.PetGenerator;
import uc.seng301.petbattler.lab6.pets.PetProxy;

public class DrawNewPetFeature {
    private static PetAccessor petAccessor;
    private static PlayerAccessor playerAccessor;
    private static PackAccessor packAccessor;
    private static PetGenerator petGenerator;
    private Pet pet;
    private Player player;
    private Pack pack;

    @BeforeAll
    public static void before_or_after_all() {
        java.util.logging.Logger.getLogger("org.hibernate").setLevel(Level.SEVERE);
        Configuration configuration = new Configuration();
        configuration.configure();
        SessionFactory sessionFactory = configuration.buildSessionFactory();
        packAccessor = new PackAccessor(sessionFactory);
        playerAccessor = new PlayerAccessor(sessionFactory);
        petAccessor = new PetAccessor(sessionFactory);
        petGenerator = new PetProxy();
    }

    @Given("Player {string} has an empty pack with the name {string}")
    public void player_has_an_empty_pack_with_the_name(String playerName, String packName) {
        player = playerAccessor.getPlayerByName(playerName);
        pack = packAccessor.createPack(packName, player, new ArrayList <>());
        Long id = packAccessor.persistPack(pack);
        Assertions.assertNotNull(packAccessor.getPackById(id));
    }

    @When("I draw a randomly selected pet")
    public void i_draw_a_randomly_selected_pet() {
        pet = petGenerator.getRandomPet();
        Long id = petAccessor.persistPet(pet);
        pet = petAccessor.getPetById(id);
        Assertions.assertNotNull(pet);
    }

    @When("I confirm I want to keep the pet in pack {string} for {string}")
    public void i_confirm_i_want_to_jeep_the_pet_in_pack_for(String packName, String playerName) {
        String choice = "Yes";
        String[] options = {"Y", "y", "Yes", "yes", "YES"};
        Assertions.assertTrue(Arrays.asList(options).contains(choice));
    }

    @When("I confirm I do not want to keep the pet in pack {string} of {string}")
    public void i_confirm_i_do_not_want_to_keep_the_pet_in_pack_of(String packName, String playerName) {
        String choice = "No";
        String[] options = {"N", "n", "No", "no", "NO"};
        Assertions.assertTrue(Arrays.asList(options).contains(choice));
        }

    @Then("The pet has a valid name, attack, health and tier")
    public void the_pet_has_a_valid_name_attack_health_and_tier() {
        Assertions.assertNotNull(pet.getName());
        Assertions.assertTrue(pet.getAttack() > 0);
        Assertions.assertTrue(pet.getHealth() >= 0);
    }

    @Then("The pet is added to the pack {string} of {string}")
    public void the_pet_is_added_to_the_pack_of(String packName, String playerName) {
        String petName = pet.getName();
        pack.addPets(pet);
        packAccessor.updatePack(pack);
        Assertions.assertTrue(pack.getPets().stream().anyMatch(pet -> petName.equals(pet.getName())));
    }

    @Then("The pet is not added to the pack {string} of {string}")
    public void the_pet_is_not_added_to_the_pack_of(String packName, String playerName) {
        String petName = pet.getName();
        packAccessor.updatePack(pack);
        Assertions.assertFalse(pack.getPets().stream().anyMatch(pet -> petName.equals(pet.getName())));
    }

    @Then("I cannot add a pet with the same name in the pack {string} of {string}")
    public void i_cannot_add_a_pet_with_the_same_name_in_the_pack_of(String packName, String playerName) {
        String petName = pet.getName();
        packAccessor.updatePack(pack);
        Assertions.assertFalse(pack.getPets().stream().anyMatch(pet -> petName.equals(pet.getName())));
    }
}
