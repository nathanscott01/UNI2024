package uc.seng301.petbattler.asg4.cucumber.step_definitions;

import java.util.logging.Level;

import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import org.junit.jupiter.api.Assertions;

import io.cucumber.java.BeforeAll;
import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import uc.seng301.petbattler.asg4.accessor.PetAccessor;
import uc.seng301.petbattler.asg4.model.Pet;

public class CreateNewPetFeature {
    private static PetAccessor petAccessor;
    private Pet pet;
    private String petName;
    private Integer petAttack;
    private Integer petHealth;
    private Exception expectedException;

    @BeforeAll
    public static void before_or_after_all() {
        java.util.logging.Logger.getLogger("org.hibernate").setLevel(Level.SEVERE);
        Configuration configuration = new Configuration();
        configuration.configure();
        SessionFactory sessionFactory = configuration.buildSessionFactory();
        petAccessor = new PetAccessor(sessionFactory);
    }

    @Given("There is no pet with name {string}")
    public void there_is_no_pet_with_name(String petName) {
        Assertions.assertNull(petAccessor.getPetByName(petName));
    }

    @When("I create a pet named {string} with attack: {int} and health: {int}")
    public void i_create_a_pet_named_with_attack_and_health(String petName, Integer attack, Integer health) {
        this.petName = petName;
        this.petAttack = attack;
        this.petHealth = health;
        Assertions.assertNotNull(this.petName);
        Assertions.assertTrue(this.petAttack > 0);
        Assertions.assertTrue(this.petHealth >= 0);
    }

    @Then("The pet is created with the correct name, attack and health")
    public void the_pet_is_created_with_the_correct_name_attack_and_health() {
        pet = petAccessor.createPet(petName, petAttack, petHealth, 1);
        Long id = petAccessor.persistPet(pet);
        pet = petAccessor.getPetById(id);
        Assertions.assertNotNull(pet);
        Assertions.assertEquals(petName, pet.getName());
        Assertions.assertEquals(petAttack, pet.getAttack());
        Assertions.assertEquals(petHealth, pet.getHealth());
    }

    @When("I create an invalid pet named {string} with attack: {int} and health: {int}")
    public void i_create_an_invalid_pet_named_with_attack_and_health(String petName, Integer attack, Integer health) {
        expectedException = Assertions.assertThrows(IllegalArgumentException.class,
                () -> petAccessor.createPet(petName, attack, health, 1));
    }

    @Then("An exception is thrown")
    public void an_exception_is_thrown() {
        Assertions.assertNotNull(expectedException);
    }
}
