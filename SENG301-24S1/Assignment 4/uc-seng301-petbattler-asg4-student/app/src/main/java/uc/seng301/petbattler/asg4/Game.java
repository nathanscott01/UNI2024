package uc.seng301.petbattler.asg4;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.IntStream;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;
import uc.seng301.petbattler.asg4.accessor.PackAccessor;
import uc.seng301.petbattler.asg4.accessor.PetAccessor;
import uc.seng301.petbattler.asg4.accessor.PlayerAccessor;
import uc.seng301.petbattler.asg4.battle.BattleRunner;
import uc.seng301.petbattler.asg4.battle.Team;
import uc.seng301.petbattler.asg4.battle.TeamList;
import uc.seng301.petbattler.asg4.cli.CommandLineInterface;
import uc.seng301.petbattler.asg4.model.GamePet;
import uc.seng301.petbattler.asg4.model.Pack;
import uc.seng301.petbattler.asg4.model.Pet;
import uc.seng301.petbattler.asg4.model.Player;
import uc.seng301.petbattler.asg4.pets.PetGenerator;
import uc.seng301.petbattler.asg4.pets.PetProxy;

/**
 * This class manages the Super Auto Pet game, including the menu items
 * @author seng301 teaching team
 */
public class Game {
    private static final Logger LOGGER = LogManager.getLogger(Game.class);
    private final CommandLineInterface cli;
    private final PlayerAccessor playerAccessor;
    private final PackAccessor packAccessor;
    private final PetAccessor petAccessor;
    private final PetGenerator petGenerator;
    private final HashMap<String, Team> teams;
    private final Random random;

    /**
     * Create a new game with default settings, including (terminal) system in and out
     */
    public Game() {
        // this will load the default config file (hibernate.cfg.xml in resources folder)
        Configuration configuration = new Configuration();
        configuration.configure();
        SessionFactory sessionFactory = configuration.buildSessionFactory();
        playerAccessor = new PlayerAccessor(sessionFactory);
        packAccessor = new PackAccessor(sessionFactory);
        petAccessor = new PetAccessor(sessionFactory);
        petGenerator = new PetProxy();
        cli = new CommandLineInterface(System.in, System.out);
        teams = new HashMap<>();
        random = new Random();
    }

    /**
     * Create a new game with custom pet generation, command line interface, and existing session
     * factory
     * 
     * @param customPetGenerator Custom pet generator implementation to get around calling the API
     * @param commandLineInterface Custom command line interface to get input from other sources
     * @param sessionFactory Existing session factory to use for accessing H2
     */
    public Game(PetGenerator customPetGenerator, CommandLineInterface commandLineInterface,
            SessionFactory sessionFactory) {
        playerAccessor = new PlayerAccessor(sessionFactory);
        packAccessor = new PackAccessor(sessionFactory);
        petAccessor = new PetAccessor(sessionFactory);
        petGenerator = customPetGenerator;
        cli = commandLineInterface;
        teams = new HashMap<>();
        random = new Random();
    }

    /**
     * Load default data so testing isn't so time consuming
     * Creates 2 players each with a pack and a team from teach
     * Can instantly battle on start with the command 'battle t1 t2'
     */
    public void loadDefault() {
        playerAccessor.persistPlayer(playerAccessor.createPlayer("Bob"));
        playerAccessor.persistPlayer(playerAccessor.createPlayer("Bailey"));

        Pack bobsPack = packAccessor.createPack("p1", playerAccessor.getPlayerByName("Bob"), new ArrayList<>());
        packAccessor.persistPack(bobsPack);
        Pack baileysPack = packAccessor.createPack("p1", playerAccessor.getPlayerByName("Bailey"), new ArrayList<>());
        packAccessor.persistPack(baileysPack);

        Pet mosquito = petAccessor.createPet("Mosquito", 5, 5, 1);
        mosquito.setEmoji("\uD83E\uDD9F");
        petAccessor.persistPet(mosquito);
        bobsPack.addPets(mosquito);
        packAccessor.updatePack(bobsPack);

        Pet duck = petAccessor.createPet("Duck", 3, 6, 1);
        duck.setEmoji("\uD83E\uDD86");
        petAccessor.persistPet(duck);
        baileysPack.addPets(duck);
        packAccessor.updatePack(baileysPack);

        teams.put("t1", new TeamList("t1", new ArrayList<>(Arrays.asList(mosquito.getGamePet(), mosquito.getGamePet(), mosquito.getGamePet()))));
        teams.put("t2", new TeamList("t2", new ArrayList<>(Arrays.asList(duck.getGamePet(), duck.getGamePet(), duck.getGamePet()))));
    }

    /**
     * Main application/game loop, handles menu items
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
                case "build_team", "bt" -> buildTeam(input);
                case "print_teams", "pt" -> printTeams();
                case "battle", "ba" -> battle(input);
                case "help" -> help();
                case "exit", "!q" -> {
                    more = false;
                    LOGGER.info("User quitting application.");
                }
                default -> {
                    cli.printLine(BAD_COMMAND);
                    LOGGER.error("User entered invalid input, {}", input);
                }
            }
        }
    }

    /**
     * Functionality to create a player
     * 
     * @param input user input to the command (including the command and params)
     */
    public void createPlayer(String input) {
        String[] uInputs = splitCommandArguments(input);
        if (uInputs.length != 2) {
            cli.printLine(BAD_COMMAND);
            LOGGER.error("User entered invalid input, {}", input);
            return;
        }
        Player player;
        try {
            player = playerAccessor.createPlayer(uInputs[1]);
        } catch (IllegalArgumentException e) {
            cli.printLine(
                    String.format("Could not create Player. %s: %s", e.getMessage(), uInputs[1]));
            return;
        }
        playerAccessor.persistPlayer(player);
        LOGGER.info("Valid input, created user {}: {}", player.getPlayerId(), player.getName());
        cli.printLine(
                String.format("Created player %d: %s", player.getPlayerId(), player.getName()));
    }

    /**
     * Functionality to create a pack of pets
     * 
     * @param input user input to the command (including the command and params)
     */
    public void createPack(String input) {
        String[] uInputs = splitCommandArguments(input);
        if (uInputs.length != 3) {
            cli.printLine(BAD_COMMAND);
            LOGGER.error("User entered invalid input, {}", input);
            return;
        }
        Player player = playerAccessor.getPlayerByName(uInputs[1]);
        if (player == null) {
            cli.printLine(String.format("No player named: %s", uInputs[1]));
            return;
        }
        Pack pack;
        try {
            pack = packAccessor.createPack(uInputs[2], player, new ArrayList<>());
        } catch (IllegalArgumentException e) {
            cli.printLine(
                    String.format("Could not create pack. %s: %s", e.getMessage(), uInputs[2]));
            return;
        }
        packAccessor.persistPack(pack);
        LOGGER.info("Created pack {} for user {} with name {}", pack.getPackId(),
                player.getPlayerId(), pack.getName());
        cli.printLine(String.format("Created pack %d: %s for %s", pack.getPackId(), pack.getName(),
                player.getName()));
    }

    /**
     * Functionality to add pets to a pack
     * 
     * @param input user input to the command (including the command and params)
     */
    public void addToPack(String input) {
        String[] uInputs = splitCommandArguments(input);
        LOGGER.info("add to pack with arguments: {}", input);
        if (uInputs.length != 3) {
            cli.printLine(BAD_COMMAND);
            LOGGER.error("User entered invalid input, {}", input);
            return;
        }
        Pack pack = packAccessor.getPackByPlayerNameAndPackName(uInputs[1], uInputs[2]);
        if (pack == null) {
            cli.printLine(String.format("No pack %s, for player %s", uInputs[2], uInputs[1]));
            LOGGER.error("No pack {}, for player {}", uInputs[2], uInputs[1]);
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
                    if(petAccessor.getPetByPackNameAndPetName(pack.getName(), pet.getName()) != null) {
                        cli.printLine("Pet not saved, already exists in pack");
                    } else {
                        try {
                            petAccessor.persistPet(pet);
                            pack.addPets(pet);
                            packAccessor.updatePack(pack);
                            cli.printLine("Pet saved");
                        } catch (IllegalArgumentException illegalArgumentException) {
                            cli.printLine("Pet could not be saved");
                            LOGGER.error(illegalArgumentException);
                        }
                    }
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
     * Functionality to build a team of pets from selected pets
     * 
     * @param input user input to the command (including the command and params)
     */
    public void buildTeam(String input) {
        String[] uInputs = splitCommandArguments(input);
        LOGGER.info("building team arguments: {}", input);
        if (uInputs.length != 4) {
            cli.printLine(BAD_COMMAND);
            LOGGER.error("User entered invalid input, {}", input);
            return;
        }
        Pack pack = packAccessor.getPackByPlayerNameAndPackName(uInputs[1], uInputs[2]);
        if (null == pack) {
            cli.printLine(String.format("No pack: %s, for player %s", uInputs[2], uInputs[1]));
            return;
        }
        if (pack.getPets().isEmpty()) {
            cli.printLine("Cannot build team with a pack with 0 pets");
            return;
        }
        if (teams.containsKey(uInputs[3])){
            cli.printLine(String.format("Team already exists with name %s", uInputs[3]));
            return;
        }
        List<GamePet> options = new ArrayList<>();
        IntStream.range(0, 5).forEach(i -> options
                .add(pack.getPets().get(random.nextInt(pack.getPets().size())).getGamePet()));
        cli.printLine(
                "Select 3 pets in desired order (front to back) by index (space separated), finish or cancel with '!q'");
        IntStream.range(0, 5)
                .forEach(i -> cli.printLine(String.format("[%d] %s", i, options.get(i).getName())));
        List<GamePet> team = new ArrayList<>();
        boolean gettingInput = true;
        while (gettingInput) {
            String[] choices = splitCommandArguments(cli.getNextLine());
            if (choices.length == 1 && choices[0].equals("!q")) {
                return;
            } else if (choices.length != 3) {
                cli.printLine("Must enter 3 pets space separated");
            } else if (Arrays.stream(choices).distinct().count() != choices.length) {
                cli.printLine("Must enter 3 unique options");
            } else {
                try {
                    Arrays.stream(choices).forEach(s -> team.add(options.get(Integer.parseInt(s))));
                    gettingInput = false;
                } catch (NumberFormatException nfe) {
                    cli.printLine("Choices must be integers in the range 0 - 4");
                }
            }
        }
        teams.put(uInputs[3], new TeamList(uInputs[3], team));
        cli.printLine(String.format("Created team %s:", uInputs[3]));

        team.forEach(gamePet -> cli.printLine(
                String.format("%s, ref: %s", gamePet.getName(), gamePet.hashCode())));
    }

    /**
     * Functionality to battle between two existing teams
     *
     * @param input user input to command, must include two existing teams
     */
    public void battle(String input) {
        String[] uInputs = splitCommandArguments(input);
        LOGGER.info("battle arguments: {}", input);
        // maybe allow only 1 team and fight against a random other team (including own)
        if (uInputs.length != 3) {
            cli.printLine(BAD_COMMAND);
            LOGGER.error("User entered invalid input, {}", input);
            return;
        }
        if (!teams.containsKey(uInputs[1])){
            cli.printLine(String.format("Team %s does not exist", uInputs[1]));
            return;
        }
        if (!teams.containsKey(uInputs[2])){
            cli.printLine(String.format("Team %s does not exist", uInputs[2]));
            return;
        }
        if (uInputs[1].equals(uInputs[2])) {
            cli.printLine("Cannot battle with duplicate teams");
            return;
        }
        new BattleRunner(cli, teams.get(uInputs[1]), teams.get(uInputs[2])).startBattle();
    }

    /**
     * Print the current teams
     */
    public void printTeams() {
        teams.forEach((teamName, team) -> {
            cli.printLine(String.format("Team: %s", teamName));
            team.forEach(p ->
                    cli.printLine(String.format("\t%s", p)));
        });
    }


    /**
     * Functionality to print a player and their packs
     * 
     * @param input user input to the command (including the command and params)
     */
    public void print(String input) {
        String[] uInputs = splitCommandArguments(input);
        if (uInputs.length != 2) {
            cli.printLine(BAD_COMMAND);
            LOGGER.error("User entered invalid input, {}", input);
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
     * Functionality for the help command
     */
    public void help() {
        cli.printLine(HELP_MESSAGE);
    }

    private static final String WELCOME_MESSAGE = """
            ######################################################
                         Welcome to SAP! Clone App
            ######################################################""";

    private static final String HELP_MESSAGE =
            """
                    Available Commands:
                    "create_player <name>" to create a new player
                    "create_pack <player_name> <pack_name>" create a pack with <pack_name> for player <player_name>
                    "add <player_name> <pack_name>" select a random pet to optionally add to pack
                    "print <player_name>" print player by name
                    "build_team <player_name> <pack_name> <team_name>" build a team of 3 pets from the selected pack. Pack must contain 1 or more pets
                    "print_teams" print the current teams available to battle
                    "battle <team_name> <team_name>" start a battle between the two teams. Teams must be distinct
                    "exit", "!q" to quit
                    "help" print this help text""";

    private static final String BAD_COMMAND = "Command incorrect use \"help\" for more information";

    /**
     * Split given string on space char, taking into consideration arguments enclosed between double
     * quotes
     * <p>
     * Adapted from aioobe's SO post - <a href="https://stackoverflow.com/a/7804472">...</a>} (CC BY-SA 3.0)
     *
     * @param commandArgs arguments to split on the space char, unless enclosed in double quotes
     * @return an array of each argument decomposed, stripping the quotes
     */
    private String[] splitCommandArguments(String commandArgs) {
        List<String> list = new ArrayList<>();
        Matcher m = Pattern.compile("([^\"]\\S*|\".+?\")\\s*").matcher(commandArgs);
        while (m.find()) {
            list.add(m.group(1).replace("\"", ""));
        }
        return list.toArray(new String[0]);
    }
}
