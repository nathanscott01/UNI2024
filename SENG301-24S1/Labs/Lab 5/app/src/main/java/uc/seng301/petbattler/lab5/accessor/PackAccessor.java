package uc.seng301.petbattler.lab5.accessor;

import java.util.ArrayList;
import java.util.List;

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import uc.seng301.petbattler.lab5.model.Pack;
import uc.seng301.petbattler.lab5.model.Pet;
import uc.seng301.petbattler.lab5.model.Player;

/**
 * This class offers helper methods for saving, removing, and fetching pack
 * records from persistence
 * {@link Pack} entities
 */
public class PackAccessor {
    private final SessionFactory sessionFactory;

    /**
     * default constructor
     *
     * @param sessionFactory the JPA session factory to talk to the persistence
     *                       implementation.
     */
    public PackAccessor(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    /**
     * Create a {@link Pack} object with the given parameters
     *
     * @param name   The Pack name must be [a-zA-Z0-9 ] (not null, empty, or only
     *               numerics)
     * @param player The Player whose pack it is (cannot be null),
     *               if not null, assumed it has been persisted.
     * @param pets   The pets to be in the pack, must not be null, but can be empty
     * @return The Pack object with given parameters
     * @throws IllegalArgumentException If any of the above preconditions for input
     *                                  arguments are violated
     */
    public Pack createPack(String name, Player player, List<Pet> pets) {
        // FIXME
        Pack pack = new Pack();
        pack.setPlayer(player);
        pack.setName(name);
        pack.setPets(pets);
        return pack;
    }

    /**
     * Get pack from persistence layer by id
     *
     * @param packId id of pack to fetch
     * @return Pack with id given if it exists in database, no user object
     */
    public Pack getPackById(Long packId) {
        if (null == packId) {
            throw new IllegalArgumentException("cannot retrieve pack with null id");
        }
        Pack pack = null;
        try (Session session = sessionFactory.openSession()) {
            pack = session.createQuery("FROM Pack WHERE packId =" + packId, Pack.class).uniqueResult();
        } catch (HibernateException e) {
            System.err.println("Unable to open session or transaction");
            e.printStackTrace();
        }
        return pack;
    }

    /**
     * Gets all packs belonging to player by id
     *
     * @param playerId id of player to fetch packs
     * @return Packs belonging to player with id provided
     */
    public List<Pack> getPlayerPacksById(Long playerId) {
        List<Pack> packs = new ArrayList<>();
        try (Session session = sessionFactory.openSession()) {
            packs = session.createQuery("FROM Pack WHERE playerId=" + playerId, Pack.class).list();
        } catch (HibernateException e) {
            System.err.println("Unable to open session or transaction");
            e.printStackTrace();
        }
        return packs;
    }

    /**
     * Save given pack to persistence
     *
     * @param pack pack to be saved
     * @return The id of the persisted pack
     */
    public Long persistPack(Pack pack) {
        try (Session session = sessionFactory.openSession()) {
            Transaction transaction = session.beginTransaction();
            session.persist(pack);
            transaction.commit();
        } catch (HibernateException e) {
            System.err.println("Unable to open session or transaction");
            e.printStackTrace();
        }
        return pack.getPackId();
    }

    /**
     * remove given pack from persistence by id
     *
     * @param packId id of pack to be deleted
     * @return true if the record is deleted
     */
    public boolean deletePackById(Long packId) throws IllegalArgumentException {
        Pack pack = getPackById(packId);
        try (Session session = sessionFactory.openSession()) {
            Transaction transaction = session.beginTransaction();
            session.remove(pack);
            transaction.commit();
            return true;
        } catch (HibernateException e) {
            System.err.println("Unable to open session or transaction");
            e.printStackTrace();
        }
        return false;
    }
}
