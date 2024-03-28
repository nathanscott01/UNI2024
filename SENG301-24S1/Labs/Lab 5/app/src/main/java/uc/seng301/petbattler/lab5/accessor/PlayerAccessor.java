package uc.seng301.petbattler.lab5.accessor;

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import uc.seng301.petbattler.lab5.model.Pet;
import uc.seng301.petbattler.lab5.model.Player;

import java.util.ArrayList;

/**
 * This class offers helper methods for saving, removing, and fetching players from persistence
 * {@link Player} entities
 */
public class PlayerAccessor {
    private final SessionFactory sessionFactory;

    /**
     * default constructor
     * @param sessionFactory the JPA session factory to talk to the persistence implementation.
     */
    public PlayerAccessor(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    /**
     * Create a {@link Player} object with the given parameters
     * @param name The Player name must be [a-zA-Z0-9] (not null, empty, or only numerics)
     * @return The Player object with given parameters
     * @throws IllegalArgumentException If any of the above preconditions for input arguments are violated
     */
    public Player createPlayer(String name) {
        if (null == name || name.isEmpty()) {
            throw new IllegalArgumentException("Name cannot be empty.");
        }
        if (name.matches("[0-9]+") || !name.matches("[a-zA-Z0-9]+")) {
            throw new IllegalArgumentException("Name be alphanumerical but cannot only be numeric");
        }
        Player player = new Player();
        player.setName(name);
        player.setPacks(new ArrayList<>());
        return player;
    }

    /**
     * Gets player from persistence by name
     * @param name name of player to fetch
     * @return Player with given name
     */
    public Player getPlayerByName(String name) {
        if (name == null || name.isBlank()) {
            throw new IllegalArgumentException("name '" + name + "' cannot be null or blank");
        }
        Player player = null;
        try (Session session = sessionFactory.openSession()) {
            player = session.createQuery("FROM Player where name='" + name + "'", Player.class).uniqueResult();
        } catch (HibernateException e) {
            System.err.println("unable to get player by name '"+name+"'");
            e.printStackTrace();
        }
        return player;
    }

    /**
     * Gets player from persistence by id
     * @param playerId id of player to fetch
     * @return Player with given id
     */
    public Player getPlayerById(Long playerId) {
        if (playerId == null) {
            throw new IllegalArgumentException("cannot retrieve player with null id");
        }
        Player player = null;
        try (Session session = sessionFactory.openSession()) {
            player = session.createQuery("FROM Player WHERE playerId =" + playerId, Player.class)
                    .uniqueResult();
        } catch (HibernateException e) {
            System.err.println("unable to get player by id '"+playerId+"'");
            e.printStackTrace();
        }
        return player;
    }


    /**
     * Saves player to persistence
     * @param player player to save
     * @return id of saved player
     * @throws IllegalArgumentException if player object is invalid (e.g. missing properties)
     */
    public Long persistPlayer(Player player) throws IllegalArgumentException {
        if (null == player || null == player.getName() || player.getName().isBlank()) {
            throw new IllegalArgumentException("cannot save null or blank player");
        }

        Player existingPlayer = getPlayerByName(player.getName());
        if (null != existingPlayer) {
            player.setPlayerId(existingPlayer.getPlayerId());
            return existingPlayer.getPlayerId();
        }

        try (Session session = sessionFactory.openSession()) {
            Transaction transaction = session.beginTransaction();
            session.persist(player);
            transaction.commit();
        } catch (HibernateException e) {
            System.err.println("unable to persist player with name '"+player.getName()+"'");
            e.printStackTrace();
        }
        return player.getPlayerId();
    }

    /**
     * remove given player from persistence by id
     * @param playerId id of player to be deleted
     * @return true if the record is deleted
     */
    public boolean removePlayerById(Long playerId) {
        Player player = getPlayerById(playerId);
        try (Session session = sessionFactory.openSession()) {
            Transaction transaction = session.beginTransaction();
            session.remove(player);
            transaction.commit();
            return true;
        } catch (HibernateException e) {
            System.err.println("unable to persist player with id '"+playerId+"'");
            e.printStackTrace();
        }
        return false;
    }
}
