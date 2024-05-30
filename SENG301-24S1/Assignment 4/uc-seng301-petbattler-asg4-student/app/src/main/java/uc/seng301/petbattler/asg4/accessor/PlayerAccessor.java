package uc.seng301.petbattler.asg4.accessor;

import java.text.Normalizer;
import java.util.ArrayList;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;

import uc.seng301.petbattler.asg4.model.Player;

/**
 * This class offers helper methods for saving, removing, and fetching {@link Player} entities
 * from persistence
 * @author seng301 teaching team
 */
public class PlayerAccessor {
    private final SessionFactory sessionFactory;
    public static final Logger LOGGER = LogManager.getLogger(PlayerAccessor.class);

    /**
     * default constructor
     * 
     * @param sessionFactory the JPA session factory to talk to the persistence
     *                       implementation.
     */
    public PlayerAccessor(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    /**
     * Create a {@link Player} object with the given parameters
     * 
     * @param name The Player name must be [a-zA-Z0-9] (not null, empty, or only
     *             numerics)
     * @return The Player object with given parameters
     * @throws IllegalArgumentException If any of the above preconditions for input
     *                                  arguments are violated
     */
    public Player createPlayer(String name) {
        LOGGER.info("Creating player with name {}", name);
        String normalisedName = Normalizer.normalize(name, Normalizer.Form.NFD)
                .replaceAll("\\p{InCombiningDiacriticalMarks}+", "");
        if (null == name || name.isBlank()) {
            throw new IllegalArgumentException("Name cannot be empty.");
        }
        if (normalisedName.matches("\\d+") || normalisedName.matches("[.-]+")
                || !normalisedName.matches("[a-zA-Z0-9 -]+")) {
            throw new IllegalArgumentException("Name be alphanumerical but cannot only be numeric");
        }
        Player player = new Player();
        player.setName(name);
        player.setPacks(new ArrayList<>());
        return player;
    }

    /**
     * Gets player from persistence by name
     * 
     * @param name name of player to fetch
     * @return Player with given name
     */
    public Player getPlayerByName(String name) {
        LOGGER.info("Getting player with name {} from persistence", name);
        Player player = null;
        try (Session session = sessionFactory.openSession()) {
            player = session.createQuery("FROM Player where name='" + name + "'", Player.class).uniqueResult();
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction", e);
        }
        return player;
    }

    /**
     * Gets player from persistence by id
     * 
     * @param playerId id of player to fetch
     * @return Player with given id
     */
    public Player getPlayerById(Long playerId) {
        LOGGER.info("Getting player with id {} from persistence", playerId);
        if (playerId == null) {
            throw new IllegalArgumentException("cannot retrieve player with null id");
        }
        Player player = null;
        try (Session session = sessionFactory.openSession()) {
            player = session.createQuery("FROM Player WHERE playerId =" + playerId, Player.class)
                    .uniqueResult();
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction", e);
        }
        return player;
    }

    /**
     * Saves player to persistence
     * 
     * @param player player to save
     * @return id of saved player
     * @throws IllegalArgumentException      if player object is invalid (e.g.
     *                                       missing properties)
     * @throws UnsupportedOperationException if given player (by name) already
     *                                       exists
     */
    public Long persistPlayer(Player player) throws IllegalArgumentException, UnsupportedOperationException {
        LOGGER.info("Save player {} to persistence", player);
        if (null == player || null == player.getName() || player.getName().isBlank()) {
            throw new IllegalArgumentException("cannot save null or blank player");
        }

        Player existingPlayer = getPlayerByName(player.getName());
        if (null != existingPlayer) {
            throw new UnsupportedOperationException("Player already exist, do you want to update instead?");
        }

        try (Session session = sessionFactory.openSession()) {
            Transaction transaction = session.beginTransaction();
            session.persist(player);
            transaction.commit();
        } catch (HibernateException e) {
            LOGGER.error("unable to persist player with name '{}'", player.getName());
            LOGGER.error(e);
        }
        return player.getPlayerId();
    }

    /**
     * remove given player from persistence by id
     * 
     * @param playerId id of player to be deleted
     * @return true if the record is deleted, false otherwise
     */
    public boolean removePlayerById(Long playerId) {
        LOGGER.info("Deleting player with id {} from persistence", playerId);
        Player player = getPlayerById(playerId);
        try (Session session = sessionFactory.openSession()) {
            Transaction transaction = session.beginTransaction();
            session.remove(player);
            transaction.commit();
            return true;
        } catch (HibernateException e) {
            LOGGER.error("Unable to open session or transaction");
            LOGGER.error(e);
        }
        return false;
    }
}
