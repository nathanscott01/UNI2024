package uc.seng301.petbattler.asg4.battle;

import uc.seng301.petbattler.asg4.cli.CommandLineInterface;
import uc.seng301.petbattler.asg4.model.GamePet;
import uc.seng301.petbattler.asg4.model.Pet;

import java.util.stream.Collectors;

/**
 * Handles battling functionality
 * @author seng301 teaching team
 */
public class BattleRunner {
    private final CommandLineInterface cli;
    private final BattlePrinter battlePrinter;
    private final Team leftTeam;
    private final Team rightTeam;

    /**
     * Create a new BattleHelper object and run a battle between two teams
     * Display depends on order of teams given, however has the same outcome
     *
     * @param cli to print to and read input from
     * @param leftTeam left team in battle
     * @param rightTeam right team in battle
     */
    public BattleRunner(CommandLineInterface cli, Team leftTeam, Team rightTeam) {
        this.cli = cli;
        this.battlePrinter = new BattlePrinter(cli);
        this.leftTeam =  leftTeam;
        this.rightTeam = rightTeam;
    }

    /**
     * Main battling functionality
     */
    public void startBattle() {
        cli.printLine("Starting Battle: ");
        battlePrinter.printBattleSnapshot(leftTeam, rightTeam);
        cli.printLine("press enter to continue");
        cli.getNextLine();
        boolean teamHasLost = false;
        int roundCounter = 0;
        while (!teamHasLost) {
            roundCounter++;
            if (roundCounter > 20) {
                // battle has been going on for too many rounds, assume some infinite loop due to abilities
                break;
            }
            cli.printLine("Round: " + roundCounter );
            // do battle
            teamHasLost = roundBattle(leftTeam, rightTeam);
            // print round outcome
            battlePrinter.printBattleSnapshot(leftTeam, rightTeam);

            if(!teamHasLost){
                // get user input to continue (or undo/redo)
                boolean gettingInput = true;
                while(gettingInput) {
                    cli.printLine("Press enter to continue, \"undo\" to go back a round, or \"redo\" to go forward a round (must have previously undone)");
                    String input = cli.getNextLine();
                    switch (input) {
                        case "" -> gettingInput = false;
                        case "undo" -> {
                            // todo: implement undo functionality
                            cli.printLine("Not implemented!");
                        }
                        case "redo" -> {
                            // todo: implement redo functionality
                            cli.printLine("Not implemented!");
                        }
                        default -> cli.printLine("Invalid option");
                    }
                }
            }
        }

        if (!teamHasLost) {
           // case where while loop exits without a winner (i.e. rounds > 20)
            cli.printLine("Game did not finish in 20 rounds. No winners this time...");
        } else {
            // print battle outcome
            if (leftTeam.getOrderedTeam().hasRemainingPets()) {
                cli.printLine(String.format("Team %s won \uD83C\uDFC6%nWelcome to the hall of fame \uD83E\uDD47%s", leftTeam.getName(), leftTeam.stream().map(Pet::getEmoji).collect(Collectors.joining(" \uD83E\uDD47"))));
            } else if (rightTeam.getOrderedTeam().hasRemainingPets()) {
                cli.printLine(String.format("Team %s won \uD83C\uDFC6%nWelcome to the hall of fame \uD83E\uDD47%s", rightTeam.getName(), rightTeam.stream().map(Pet::getEmoji).collect(Collectors.joining(" \uD83E\uDD47"))));
            } else {
                cli.printLine("No winners this time...");
            }
        }
    }


    /**
     * Run battle simulation for one round, return true iff one or more teams are out of pets
     * @param leftTeam left team in battle
     * @param rightTeam right team in battle
     * @return true if left and/or right team have no remaining pets after the round simulation
     */
    public boolean roundBattle(Team leftTeam, Team rightTeam) {
        boolean gameIsOver = false;
        TeamOrdering leftTeamOrdering = leftTeam.getOrderedTeam();
        TeamOrdering rightTeamOrdering = rightTeam.getOrderedTeam();
        try {
            GamePet l = leftTeamOrdering.getNextPet();
            GamePet r = rightTeamOrdering.getNextPet();
            r.takeDamage(l.getAttack());
            cli.printLine(String.format("[%s attacks %s for %d]", l.getEmoji(), r.getEmoji(), l.getAttack()));
            l.takeDamage(r.getAttack());
            cli.printLine(String.format("[%s attacks %s for %d]", r.getEmoji(), l.getEmoji(), r.getAttack()));
                if (l.getHealth() <= 0) {
                    cli.printLine(String.format("[%s fainted]", l.getEmoji()));
                    if(!leftTeamOrdering.hasRemainingPets()) {
                        gameIsOver = true;
                    }
                } else {
                    l.getSpecialAbility().useSpecialAbility(l, r, cli);
                }
                if (r.getHealth() <= 0) {
                    cli.printLine(String.format("[%s fainted]", r.getEmoji()));
                    if(!rightTeamOrdering.hasRemainingPets()) {
                        gameIsOver = true;
                    }
                } else {
                    r.getSpecialAbility().useSpecialAbility(r, l, cli);
                }
        } catch (NoRemainingPetsException noRemainingPetsException) {
            gameIsOver = true;
        }
        return gameIsOver;
    }

}
