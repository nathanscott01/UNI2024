package uc.seng301.petbattler.asg4.accessor;

import java.text.Normalizer;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import uc.seng301.petbattler.asg4.model.Pack;
import uc.seng301.petbattler.asg4.model.Pet;

/**
 * This class offers helper methods for saving, removing, and fetching {@link Pet} entities
 * from persistence
 * @author seng301 teaching team
 */
public class PetAccessor {
    private final SessionFactory sessionFactory;
    public static final Logger LOGGER = LogManager.getLogger(PetAccessor.class);

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
     * @param name   the pet name (not null, empty, or only numerics, can be
     *               [a-zA-Z0-9 ])
     * @param attack attack value of pet (must be > 0)
     * @param health health value of pet (must be >= 0)
     * @param tier   tier of the pet (aka level, must be > 0)
     * @return The Pet object with given parameters
     * @throws IllegalArgumentException if any of the above preconditions for input
     *                                  arguments are violated
     */
    public Pet createPet(String name, int attack, int health, int tier) {
        LOGGER.info("Creating pet with name {}, attack {}, health {}", name, attack, health);
        String normalisedName = Normalizer.normalize(name, Normalizer.Form.NFD)
                .replaceAll("\\p{InCombiningDiacriticalMarks}+", "");
        if (null == name || name.isBlank()) {
            throw new IllegalArgumentException("Name cannot be empty.");
        }
        if (normalisedName.matches("\\d+") || !normalisedName.matches("[a-zA-Z0-9 ]+")) {
            throw new IllegalArgumentException("Name must be alphanumerical but cannot only be numeric");
        }
        if (attack <= 0) {
            throw new IllegalArgumentException("Attack must be strictly positive");
        }
        if (health < 0) {
            throw new IllegalArgumentException("Health must be positive");
        }
        if (tier <= 0) {
            throw new IllegalArgumentException("Tier must be positive");
        }
        Pet pet = new Pet();
        pet.setName(name);
        pet.setAttack(attack);
        pet.setHealth(health);
        pet.setTier(tier);
        return pet;
    }

    /**
     * Get pet from persistence layer by its id
     *
     * @param petId id of pet to fetch
     * @return the pet with id given if it exists in database, no user object
     */
    public Pet getPetById(Long petId) {
        LOGGER.info("Getting pet with id {} from persistence", petId);
        Pet pet = null;
        try (Session session = sessionFactory.openSession()) {
            pet = session.createQuery("FROM Pet WHERE petId =" + petId, Pet.class).uniqueResult();
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction", e);
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
        LOGGER.info("Getting pet with name {} from persistence", petName);
        Pet pet = null;
        try (Session session = sessionFactory.openSession()) {
            pet = session.createQuery("FROM Pet WHERE name ='" + petName + "'", Pet.class).uniqueResult();
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction", e);
        }
        return pet;
    }

    /**
     * Get pet from persistence layer by pack name and pet name
     *
     * @param packName name of pack the pet belongs to
     * @param petName name of pet
     * @return The matching pack, null if none could be found
     */
    public Pet getPetByPackNameAndPetName(String packName, String petName) {
        LOGGER.info("Getting pet from persistence by pack name {} and pet name {}", packName, petName);
        Pet pet = null;
        try (Session session = sessionFactory.openSession()) {
            Pack pack =
                    session.createQuery("FROM Pack WHERE name='" + packName + "'", Pack.class)
                            .uniqueResult();
            if (null != pack && null != pack.getPets()) {
                Optional<Pet> petToFind = pack.getPets().stream()
                        .filter(p -> petName.equals(p.getName())).findFirst();
                pet = petToFind.orElse(null);
            }
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction", e);
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
        LOGGER.info("Getting list of pets in pack id {} from persistence", packId);
        List<Pet> pets = new ArrayList<>();
        try (Session session = sessionFactory.openSession()) {
            pets = session.createQuery("FROM Pet WHERE packId=" + packId, Pet.class).list();
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction", e);
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
        LOGGER.info("Persisting pet {}", pet);
        try (Session session = sessionFactory.openSession()) {
            Transaction transaction = session.beginTransaction();
            session.persist(pet);
            transaction.commit();
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction", e);
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
        LOGGER.info("Deleting pet with id {} from persistence", petId);
        Pet pet = getPetById(petId);
        try (Session session = sessionFactory.openSession()) {
            Transaction transaction = session.beginTransaction();
            session.remove(pet);
            transaction.commit();
            return true;
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction", e);
        }
        return false;
    }
}
