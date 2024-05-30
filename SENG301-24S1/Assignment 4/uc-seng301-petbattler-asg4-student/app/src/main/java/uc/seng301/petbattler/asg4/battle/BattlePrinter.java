package uc.seng301.petbattler.asg4.battle;
import uc.seng301.petbattler.asg4.cli.CommandLineInterface;
import uc.seng301.petbattler.asg4.model.GamePet;

/**
 * Class to print battle lineup to CLI
 * @author seng301 teaching team
 */
public class BattlePrinter {

    private final CommandLineInterface cli;

    /**
     * Create a new battle printer that prints to the given interface
     * @param cli interface to print to
     */
    public BattlePrinter(CommandLineInterface cli) {
        this.cli = cli;
    }

    /**
     * Print a battle snapshot
     * @param leftTeam team on left side of battle
     * @param rightTeam team on right side of battle
     */
    public void printBattleSnapshot(Team leftTeam, Team rightTeam) {
        StringBuilder nameRow = new StringBuilder();
        StringBuilder emojiRow = new StringBuilder();
        StringBuilder statRow = new StringBuilder();

        // print left team (reversed for correct ordering on display)
        teamPrinter(leftTeam.getReversedTeam(), nameRow, emojiRow, statRow, true);

        // print right team
        teamPrinter(rightTeam.getOrderedTeam(), nameRow, emojiRow, statRow, false);

        // print built strings in order
        cli.printLine(String.valueOf(nameRow));
        cli.printLine(String.valueOf(emojiRow));
        cli.printLine(String.valueOf(statRow));
    }

    /**
     * Print a specific team adding to the existing strings
     * @param team team to print
     * @param nameRow current name row string
     * @param emojiRow current emoji (pet) row string
     * @param statRow current stat row string
     * @param isFirstTeam add spacing and "V" at the end if printing first team
     */
    private void teamPrinter(TeamOrdering team, StringBuilder nameRow, StringBuilder emojiRow, StringBuilder statRow, boolean isFirstTeam) {
        while(team.hasRemainingPets()) {
            GamePet pet = team.getNextPet();
            int nameLength = pet.getName().length();
            int paddingAmount = nameLength>9 ? 1 :  (11- nameLength)/2;
            int length = nameLength + paddingAmount + paddingAmount;
            // add name (find min size to add padding if needed)
            nameRow.append(String.format("|%s%s%s", " ".repeat(paddingAmount), pet.getName(), " ".repeat(paddingAmount)));
            // add emoji with padding
            emojiRow.append(String.format("|%s%s%s", " ".repeat(length/2 -(length%2!= 0 ? 0 :1)), pet.getEmoji(), " ".repeat(length/2 - 1)));
            // add stats with padding
            statRow.append(String.format("|%s%s%s", " ".repeat((length-pet.getStatsString().length())/2 + ((length+pet.getStatsString().length())%2!=0?1:0)), pet.getStatsString(), " ".repeat((length-pet.getStatsString().length())/2)));
        }
        nameRow.append ("|");
        emojiRow.append("|");
        statRow.append ("|");
        if (isFirstTeam) {
            nameRow.append ("     ");
            emojiRow.append("  V  ");
            statRow.append ("     ");
        }
    }
}