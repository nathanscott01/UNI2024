package uc.seng301.petbattler.lab5;

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;
import uc.seng301.petbattler.lab5.model.Pack;
import uc.seng301.petbattler.lab5.model.Pet;
import uc.seng301.petbattler.lab5.model.Player;

import java.util.logging.Level;

public class App {
    private static SessionFactory sessionFactory;

    public App() {
        // this will load the config file (hibernate.cfg.xml in resources folder)
        Configuration configuration = new Configuration();
        configuration.configure();
        sessionFactory = configuration.buildSessionFactory();
    }

    public static void main(String[] args) {
        java.util.logging.Logger.getLogger("org.hibernate").setLevel(Level.SEVERE);
        new App();

        Player player = new Player();
        player.setName("Jane");

        Pack pack = new Pack();
        pack.setName("Jane's First Pack");
        pack.setPlayer(player);

        Pet ant = new Pet();
        ant.setName("Ant");
        ant.setAttack(2);
        ant.setHealth(2);
        ant.setPack(pack);

        Pet beaver = new Pet();
        beaver.setName("Minotaur");
        beaver.setAttack(3);
        beaver.setHealth(2);
        beaver.setPack(pack);

        Transaction transaction = null;
        Long playerId = -1L;
        try (Session session = sessionFactory.openSession()) {
            System.out.println("Persisting a player with pack of pets");
            transaction = session.beginTransaction();
            session.persist(player);
            playerId = player.getPlayerId();
            session.persist(pack);
            session.persist(ant);
            session.persist(beaver);
            // persist into the database
            transaction.commit();
        } catch (HibernateException e) {
            System.err.println("Unable to open session or transaction");
            e.printStackTrace();
            if (transaction != null) {
                transaction.rollback();
            }
        }

        try (Session session = sessionFactory.openSession()) {
            System.out.println("Retrieving player with id: " + playerId);
            // note that HQL queries use the Java attributes names, i.e. playerId
            // (attribute) and not id_player (table column)
            Player retrievedPlayer = session.createQuery("FROM Player WHERE playerId =" + playerId, Player.class)
                    .uniqueResult();
            System.out.println(retrievedPlayer);
        } catch (HibernateException e) {
            System.err.println("Unable to open session or transaction");
            e.printStackTrace();
        }
    }
}
