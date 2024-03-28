package uc.seng301.petbattler.lab5.accessor;

import java.util.ArrayList;
import java.util.List;

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import uc.seng301.petbattler.lab5.model.Pet;

/**
 * This class offers helper methods for saving, removing, and fetching pet
 * records from persistence
 * {@link Pet} entities
 */
public class PetAccessor {
    private final SessionFactory sessionFactory;

    /**
     * default constructor
     *
     * @param sessionFactory the JPA session factory to talk to the persistence
     *                       implementation.
     */
    public PetAccessor(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    /**
     * Create a {@link Pet} object with the given parameters
     *
     * @param name   the pet name (not null, not empty, unique, or not only
     *               numerics, can be
     *               [a-zA-Z0-9 ])
     * @param attack attack value of pet (must be > 0)
     * @param health health value of pet (must be >= 0)
     * @return The Card object with given parameters
     * @throws IllegalArgumentException if any of the above preconditions for input
     *                                  arguments are violated
     */
    public Pet createPet(String name, int attack, int health) {
        if (null == name || name.isEmpty()) {
            throw new IllegalArgumentException("Name cannot be empty.");
        }
        if (name.matches("\\d+") || !name.matches("[a-zA-Z0-9 ]+")) {
            throw new IllegalArgumentException("Name must be alphanumerical but cannot only be numeric");
        }
        if (attack <= 0) {
            throw new IllegalArgumentException("Attack must be strictly positive");
        }
        if (health <= 0) {
            throw new IllegalArgumentException("Health must be positive");
        }
        if (null != getPetByName(name)) {
            throw new IllegalArgumentException(String.format("Pet with name %s already exists", name));
        }
        Pet pet = new Pet();
        pet.setName(name);
        pet.setAttack(attack);
        pet.setHealth(health);
        return pet;
    }

    /**
     * Get pet from persistence layer by its id
     *
     * @param petId id of pet to fetch
     * @return the pet with id given if it exists in database, no user object
     */
    public Pet getPetById(Long petId) {
        if (null == petId) {
            throw new IllegalArgumentException("cannot retrieve card with null id");
        }
        Pet pet = null;
        try (Session session = sessionFactory.openSession()) {
            pet = session.createQuery("FROM Pet WHERE petId =" + petId, Pet.class).uniqueResult();
        } catch (HibernateException e) {
            System.err.println("Unable to open session or transaction");
            e.printStackTrace();
        }
        return pet;
    }

    /**
     * Get a pet from persistence layer by its name
     *
     * @param petName a name to look for
     * @return the pet with given name if such card exists, null otherwise
     */
    public Pet getPetByName(String petName) {
        Pet pet = null;
        try (Session session = sessionFactory.openSession()) {
            pet = session.createQuery("FROM Pet WHERE name ='" + petName + "'", Pet.class).uniqueResult();
        } catch (HibernateException e) {
            System.err.println("Unable to open session or transaction");
            e.printStackTrace();
        }
        return pet;
    }

    /**
     * Gets all pets belonging to a pack by id
     *
     * @param packId id of pack to get pets from
     * @return Pets belonging to pack with id provided
     */
    public List<Pet> getPackPetsById(Long packId) {
        List<Pet> pets = new ArrayList<>();
        try (Session session = sessionFactory.openSession()) {
            pets = session.createQuery("FROM Pet WHERE packId=" + packId, Pet.class).list();
        } catch (HibernateException e) {
            System.err.println("Unable to open session or transaction");
            e.printStackTrace();
        }
        return pets;
    }

    /**
     * Save given pet to persistence
     *
     * @param pet pet to be saved
     * @return The id of the persisted pet
     */
    public Long persistPet(Pet pet) {
        try (Session session = sessionFactory.openSession()) {
            Transaction transaction = session.beginTransaction();
            session.persist(pet);
            transaction.commit();
        } catch (HibernateException e) {
            System.err.println("Unable to open session or transaction");
            e.printStackTrace();
        }
        return pet.getPetId();
    }

    /**
     * remove given pet from persistence by id
     *
     * @param petId id of pet to be deleted
     * @return true if the record is deleted
     */
    public boolean deletePetById(Long petId) throws IllegalArgumentException {
        Pet pet = getPetById(petId);
        try (Session session = sessionFactory.openSession()) {
            Transaction transaction = session.beginTransaction();
            session.remove(pet);
            transaction.commit();
            return true;
        } catch (HibernateException e) {
            System.err.println("Unable to open session or transaction");
            e.printStackTrace();
        }
        return false;
    }
}
