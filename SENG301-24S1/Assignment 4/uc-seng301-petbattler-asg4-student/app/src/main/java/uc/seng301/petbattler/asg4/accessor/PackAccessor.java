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
import uc.seng301.petbattler.asg4.model.Player;

/**
 * This class offers helper methods for saving, removing, and fetching {@link Pack} entities
 * from persistence
 * @author seng301 teaching team
 */
public class PackAccessor {
    private static final Logger LOGGER = LogManager.getLogger(PackAccessor.class);
    private final SessionFactory sessionFactory;

    /**
     * default constructor
     *
     * @param sessionFactory the JPA session factory to talk to the persistence implementation.
     */
    public PackAccessor(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    /**
     * Create a {@link Pack} object with the given parameters
     *
     * @param name The Pack name must be [a-zA-Z0-9 ] (not null, empty, or only numerics)
     * @param player The Player whose pack it is (cannot be null)
     * @param pets The pets to be in the pack, must not be null and must have at least 1 card
     * @return The Pack object with given parameters
     * @throws IllegalArgumentException If any of the above preconditions for input arguments are
     *         violated
     */
    public Pack createPack(String name, Player player, List<Pet> pets) {
        LOGGER.info("Creating pack name {} for player {}", name, player);
        String normalisedName = Normalizer.normalize(name, Normalizer.Form.NFD)
                .replaceAll("\\p{InCombiningDiacriticalMarks}+", "");
        if (name == null || name.isBlank()) {
            throw new IllegalArgumentException("Name cannot be empty.");
        }
        if (normalisedName.matches("\\d+") || !normalisedName.matches("[a-zA-Z0-9 ]+")) {
            throw new IllegalArgumentException(
                    "Name must be alphanumerical but cannot only be numeric");
        }
        if (null == player) {
            throw new IllegalArgumentException("Player must exist");
        }
        if (!player.getPacks().stream().filter(pack -> pack.getName().equals(name)).toList()
                .isEmpty()) {
            throw new IllegalArgumentException("A player's pack names must be unique");
        }
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
     * @return Pack with id given if it exists in database, no player object attached; null if not
     *         found
     */
    public Pack getPackById(Long packId) {
        LOGGER.info("Getting pack with id {} from persistence", packId);
        Pack pack = null;
        try (Session session = sessionFactory.openSession()) {
            pack = session.createQuery("FROM Pack WHERE packId =" + packId, Pack.class)
                    .uniqueResult();
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction", e);
        }
        return pack;
    }

    /**
     * Gets all packs belonging to player by id
     *
     * @param playerId id of player to fetch packs
     * @return Packs belonging to player with id provided, empty list if not found
     */
    public List<Pack> getPlayerPacksById(Long playerId) {
        LOGGER.info("Getting list of packs owned by player id {} from persistence", playerId);
        List<Pack> packs = new ArrayList<>();
        try (Session session = sessionFactory.openSession()) {
            packs = session.createQuery("FROM Pack WHERE playerId=" + playerId, Pack.class).list();
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction", e);
        }
        return packs;
    }

    /**
     * Save given pack to persistence
     *
     * @param pack pack to be saved, assumed not null
     * @return The id of the persisted pack
     * @throws UnsupportedOperationException if the pack already exists and should be updated
     *         instead
     */
    public Long persistPack(Pack pack) throws UnsupportedOperationException {
        LOGGER.info("Persisting pack {}", pack);
        if (null != pack.getPackId() && null != getPackById(pack.getPackId())) {
            throw new UnsupportedOperationException(
                    "Pack already exists, do you want to updatePack() instead?");
        }
        try (Session session = sessionFactory.openSession()) {
            Transaction transaction = session.beginTransaction();
            session.persist(pack);
            transaction.commit();
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction", e);
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
        LOGGER.info("Deleting pack with id {} from persistence", packId);
        Pack pack = getPackById(packId);
        try (Session session = sessionFactory.openSession()) {
            Transaction transaction = session.beginTransaction();
            session.remove(pack);
            transaction.commit();
            return true;
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction", e);
        }
        return false;
    }

    /**
     * Get pack from persistence layer by player name and pack name
     *
     * @param playerName name of player who owns the pack
     * @param packName name of pack
     * @return The matching pack, null if none could be found
     */
    public Pack getPackByPlayerNameAndPackName(String playerName, String packName) {
        LOGGER.info("Getting pack from persistence by player name {} and pack name {}", playerName,
                packName);
        Pack pack = null;
        try (Session session = sessionFactory.openSession()) {
            Player player =
                    session.createQuery("FROM Player WHERE name='" + playerName + "'", Player.class)
                            .uniqueResult();
            if (null != player && null != player.getPacks()) {
                Optional<Pack> packToFind = player.getPacks().stream()
                        .filter(p -> packName.equals(p.getName())).findFirst();
                pack = packToFind.orElse(null);
            }
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction", e);
        }
        return pack;
    }

    /**
     * Update given pack, must already exist in persistence
     *
     * @param pack pack to updated
     * @return The id of the updated pack
     */
    public long updatePack(Pack pack) throws UnsupportedOperationException {
        LOGGER.info("Update existing pack object {}", pack);
        if (pack.getPackId() == -1L) {
            throw new UnsupportedOperationException(
                    "Pack has not been persisted, use persistPack() instead");
        }
        try (Session session = sessionFactory.openSession()) {
            Transaction transaction = session.beginTransaction();
            session.merge(pack);
            transaction.commit();
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction", e);
        }
        return pack.getPackId();
    }
}
