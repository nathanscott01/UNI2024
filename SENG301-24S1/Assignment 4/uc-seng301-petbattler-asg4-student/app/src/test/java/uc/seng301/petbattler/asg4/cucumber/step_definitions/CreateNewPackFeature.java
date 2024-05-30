package uc.seng301.petbattler.asg4.cucumber.step_definitions;

import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;

import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.junit.jupiter.api.Assertions;

import io.cucumber.java.BeforeAll;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import uc.seng301.petbattler.asg4.accessor.PackAccessor;
import uc.seng301.petbattler.asg4.accessor.PetAccessor;
import uc.seng301.petbattler.asg4.accessor.PlayerAccessor;
import uc.seng301.petbattler.asg4.model.Pack;
import uc.seng301.petbattler.asg4.model.Pet;
import uc.seng301.petbattler.asg4.model.Player;

public class CreateNewPackFeature {
    private static PackAccessor packAccessor;
    private static PlayerAccessor playerAccessor;
    private static PetAccessor petAccessor;

    @BeforeAll
    public static void before_or_after_all() {
        java.util.logging.Logger.getLogger("org.hibernate").setLevel(Level.SEVERE);
        Configuration configuration = new Configuration();
        configuration.configure();
        SessionFactory sessionFactory = configuration.buildSessionFactory();
        packAccessor = new PackAccessor(sessionFactory);
        playerAccessor = new PlayerAccessor(sessionFactory);
        petAccessor = new PetAccessor(sessionFactory);
    }

    // AC 1.1, 2, 3
    @Given("I create a player named {string}")
    public void i_create_a_player_named(String playerName) {
        Player player = playerAccessor.createPlayer(playerName);
        Long id = playerAccessor.persistPlayer(player);
        Assertions.assertNotNull(playerAccessor.getPlayerById(id));
    }

    // AC1.1
    @Given("Player {string} has no packs with the name {string}")
    public void player_has_no_packs_with_the_name(String playerName, String packName) {
        Player player = playerAccessor.getPlayerByName(playerName);
        Assertions.assertTrue(player.getPacks().stream().noneMatch(pack -> packName.equals(pack.getName())));
    }

    // AC2
    @Given("Player {string} exists")
    public void player_exists(String playerName) {
        Assertions.assertNotNull(playerAccessor.getPlayerByName(playerName));
    }

    // AC2
    @Given("Player {string} already has a pack with the name {string}")
    public void player_already_has_a_pack_with_the_name(String playerName, String packName) {
        Player player = playerAccessor.getPlayerByName(playerName);
        Pack pack = packAccessor.createPack(packName, player, new ArrayList<>());
        Long id = packAccessor.persistPack(pack);
        Assertions.assertNotNull(packAccessor.getPackById(id));
    }

    // AC1.1, 2, 3
    @When("I create the pack with name {string} for {string}")
    public void i_create_the_pack_with_name_for(String packName, String playerName) {
        Player player = playerAccessor.getPlayerByName(playerName);
        Pack pack = packAccessor.createPack(packName, player, new ArrayList<>());
        Long id = packAccessor.persistPack(pack);
        Assertions.assertNotNull(packAccessor.getPackById(id));
    }

    // AC1.1
    @Then("The pack is created with name {string} for {string}")
    public void the_pack_is_created_with_name_for(String packName, String playerName) {
        Player player = playerAccessor.getPlayerByName(playerName);
        Assertions.assertTrue(player.getPacks().stream().anyMatch(pack -> packName.equals(pack.getName())));
    }

    // AC1.2
    @Then("I am not allowed to create the pack with name {string} for {string}")
    public void i_am_not_allowed_to_create_the_pack_with_name_for(String packName, String playerName) {
        Player player = playerAccessor.getPlayerByName(playerName);
        List<Pet> pets = new ArrayList<>();
        Assertions.assertThrows(IllegalArgumentException.class, () -> packAccessor.createPack(packName, player, pets));
    }

    // AC3
    @When("I add a pet named {string} with attack {int} and health {int} in pack {string} for {string}")
    public void i_add_a_pet_named_with_attack_and_health_in_pack_for(String petName, Integer attack, Integer health,
            String packName, String playerName) {
        Pet pet = petAccessor.createPet(petName, attack, health, 1);
        Long id = petAccessor.persistPet(pet);
        Assertions.assertNotNull(pet = petAccessor.getPetById(id));
        Player player = playerAccessor.getPlayerByName(playerName);
        Assertions.assertNotNull(player);
        Pack pack = player.getPacks().stream().filter(p -> packName.equals(p.getName())).findFirst().orElse(null);
        Assertions.assertNotNull(pack);
        pack.addPets(pet);
        packAccessor.updatePack(pack);
    }

    // AC3
    @Then("The pack {string} of {string} includes a pet named {string}")
    public void the_pack_of_includes_a_pet_named(String packName, String playerName, String petName) {
        Player player = playerAccessor.getPlayerByName(playerName);
        Pack pack = player.getPacks().stream().filter(p -> packName.equals(p.getName())).findFirst().orElse(null);
        Assertions.assertTrue(pack.getPets().stream().anyMatch(pet -> petName.equals(pet.getName())));
    }
}
