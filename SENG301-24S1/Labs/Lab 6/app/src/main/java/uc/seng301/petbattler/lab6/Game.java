package uc.seng301.petbattler.lab6;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

import uc.seng301.petbattler.lab6.accessor.PackAccessor;
import uc.seng301.petbattler.lab6.accessor.PetAccessor;
import uc.seng301.petbattler.lab6.accessor.PlayerAccessor;
import uc.seng301.petbattler.lab6.cli.CommandLineInterface;
import uc.seng301.petbattler.lab6.model.Pack;
import uc.seng301.petbattler.lab6.model.Pet;
import uc.seng301.petbattler.lab6.model.Player;
import uc.seng301.petbattler.lab6.pets.PetGenerator;
import uc.seng301.petbattler.lab6.pets.PetProxy;

/**
 * Main game loop functionality for application
 */
public class Game {
    private static final Logger LOGGER = LogManager.getLogger(Game.class);
    private final CommandLineInterface cli;
    private final PlayerAccessor playerAccessor;
    private final PackAccessor packAccessor;
    private final PetAccessor petAccessor;
    private final PetGenerator petGenerator;

    /**
     * Create a new game with default settings
     */
    public Game() {
        // this will load the config file (hibernate.cfg.xml in resources folder)
        Configuration configuration = new Configuration();
        configuration.configure();
        SessionFactory sessionFactory = configuration.buildSessionFactory();
        playerAccessor = new PlayerAccessor(sessionFactory);
        packAccessor = new PackAccessor(sessionFactory);
        petAccessor = new PetAccessor(sessionFactory);
        petGenerator = new PetProxy();
        cli = new CommandLineInterface(System.in, System.out);
    }

    /**
     * Create a new game with custom pet generation, command line interface, and
     * existing session factory
     * 
     * @param customPetGenerator   Custom pet generator implementation to get around
     *                             calling the API
     * @param commandLineInterface Custom command line interface to get input from
     *                             other sources
     * @param sessionFactory       Existing session factory to use for accessing H2
     */
    public Game(PetGenerator customPetGenerator, CommandLineInterface commandLineInterface,
            SessionFactory sessionFactory) {
        playerAccessor = new PlayerAccessor(sessionFactory);
        packAccessor = new PackAccessor(sessionFactory);
        petAccessor = new PetAccessor(sessionFactory);
        petGenerator = customPetGenerator;
        cli = commandLineInterface;
    }

    /**
     * Main application/game loop
     */
    public void play() {
        boolean more = true;
        cli.printLine(WELCOME_MESSAGE);
        cli.printLine(HELP_MESSAGE);
        while (more) {
            String input = cli.getNextLine();
            LOGGER.info("User input: {}", input);
            switch (input.split(" ")[0]) {
                case "create_player", "cpl" -> createPlayer(input);
                case "create_pack", "cpa" -> createPack(input);
                case "add" -> addToPack(input);
                case "print" -> print(input);
                case "exit", "!q" -> {
                    more = false;
                    exit();
                }
                case "help" -> help();
                default -> {
                    cli.printLine(BAD_COMMAND);
                    LOGGER.info("User entered invalid input, {}", input);
                }
            }
        }
    }

    /**
     * Functionality for the create_player command
     * 
     * @param input user input to the command
     */
    public void createPlayer(String input) {
        String[] uInputs = splitCommandArguments(input);
        Player player;
        if (uInputs.length != 2) {
            cli.printLine(BAD_COMMAND);
            return;
        }
        uInputs[1] = uInputs[1].replace("\"", "");
        try {
            player = playerAccessor.createPlayer(uInputs[1]);
        } catch (IllegalArgumentException e) {
            cli.printLine(String.format("Could not create Player. %s: %s", e.getMessage(), uInputs[1]));
            return;
        }
        playerAccessor.persistPlayer(player);
        LOGGER.info("Valid input, created user {}: {}", player.getPlayerId(), player.getName());
        cli.printLine(String.format("Created player %d: %s", player.getPlayerId(), player.getName()));
    }

    /**
     * Functionality for the create_deck command
     * 
     * @param input user input to the command
     */
    public void createPack(String input) {
        String[] uInputs = splitCommandArguments(input);
        Pack pack;
        if (uInputs.length != 3) {
            cli.printLine(BAD_COMMAND);
            return;
        }
        uInputs[1] = uInputs[1].replace("\"", "");
        Player player = playerAccessor.getPlayerByName(uInputs[1]);
        if (player == null) {
            cli.printLine(String.format("No player named: %s", uInputs[1]));
            return;
        }
        try {
            pack = packAccessor.createPack(uInputs[2], player, new ArrayList<>());
        } catch (IllegalArgumentException e) {
            cli.printLine(String.format("Could not create pack. %s: %s", e.getMessage(), uInputs[2]));
            return;
        }
        packAccessor.persistPack(pack);
        LOGGER.info("Valid input, created pack {} for user {} with name {}", pack.getPackId(), player.getPlayerId(),
                pack.getName());
        cli.printLine(String.format("Created pack %d: %s for %s", pack.getPackId(), pack.getName(), player.getName()));
    }

    /**
     * Functionality for the fillPack command to add pets to the pack
     * 
     * @param input user input to the command
     */
    public void addToPack(String input) {
        String[] uInputs = splitCommandArguments(input);
        LOGGER.info("add to pack with arguments: %s", input);
        if (uInputs.length != 3) {
            cli.printLine(BAD_COMMAND);
            return;
        }
        uInputs[1] = uInputs[1].replace("\"", "");
        uInputs[2] = uInputs[2].replace("\"", "");
        Pack pack = packAccessor.getPackByPlayerNameAndPackName(uInputs[1], uInputs[2]);
        if (pack == null) {
            cli.printLine(String.format("No pack: %s, for player %s", uInputs[2], uInputs[1]));
            return;
        }
        Pet pet = petGenerator.getRandomPet();
        cli.printLine("You drew...");
        cli.printLine(pet.toString());
        cli.printLine("Do you want to add this pet to your pack? Y/N");
        String choice;
        boolean gettingInput = true;
        while (gettingInput) {
            choice = cli.getNextLine();
            switch (choice.split(" ")[0]) {
                case "Y", "y", "Yes", "yes", "YES" -> {
                    // we may have drawn a pet we already persisted
                    if (null == petAccessor.getPetByName(pet.getName())) {
                        petAccessor.persistPet(pet);
                    }
                    pack.addPets(pet);
                    packAccessor.updatePack(pack);
                    cli.printLine("Pet saved");
                    gettingInput = false;
                }
                case "N", "n", "No", "no", "NO" -> {
                    cli.printLine("Pet not saved");
                    gettingInput = false;
                }
                default -> {
                    cli.printLine("Invalid option please input Yes or No");
                    gettingInput = false;
                }
            }
        }
    }

    /**
     * Functionality for the print command
     * 
     * @param input user input to the command
     */
    public void print(String input) {
        String[] uInputs = splitCommandArguments(input);
        if (uInputs.length != 2) {
            cli.printLine(BAD_COMMAND);
            return;
        }
        Player player = playerAccessor.getPlayerByName(uInputs[1]);
        if (player == null) {
            cli.printLine(String.format("No player named: %s", uInputs[1]));
            return;
        }
        cli.printLine(player.toString());
    }

    /**
     * Functionality for the exit command
     */
    public void exit() {
        LOGGER.info("User quitting application.");
    }

    /**
     * Functionality for the help command
     */
    public void help() {
        cli.printLine(HELP_MESSAGE);
    }

    private static final String WELCOME_MESSAGE = """
            ######################################################
                         Welcome to SAP! Clone App
            ######################################################""";

    private static final String HELP_MESSAGE = """
            Available Commands:
            "create_player <name>" to create a new player
            "create_pack <player_name> <pack_name>" create a pack with <pack_name> for player <player_name>
            "add <player_name> <pack_name>" select a random pet to optionally add to pack
            "print <player_name>" print player by name
            "exit", "!q" to quit
            "help" print this help text""";

    private static final String BAD_COMMAND = "Command incorrect use \"help\" for more information";

    /**
     * Split given string on space char, taking into consideration arguments
     * enclosed between double quotes
     * 
     * Adapted from aioobe's SO post - https://stackoverflow.com/a/7804472
     * (CC BY-SA 3.0)
     * 
     * @param commandArgs arguments to split on the space char, unless enclosed in
     *                    double quotes
     * @return an array of each argument decomposed, stripping the quotes
     */
    private String[] splitCommandArguments(String commandAgrs) {
        List<String> list = new ArrayList<>();
        Matcher m = Pattern.compile("([^\"]\\S*|\".+?\")\\s*").matcher(commandAgrs);
        while (m.find()) {
            list.add(m.group(1).replace("\"", ""));
        }
        return list.toArray(new String[0]);
    }

}
