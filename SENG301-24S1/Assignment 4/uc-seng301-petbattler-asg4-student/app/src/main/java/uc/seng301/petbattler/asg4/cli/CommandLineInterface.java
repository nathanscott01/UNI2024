package uc.seng301.petbattler.asg4.cli;

import java.io.InputStream;
import java.io.PrintStream;
import java.util.Scanner;

/**
 * Interface for handling command line input to the application
 * @author seng301 teaching team
 */
public class CommandLineInterface {
    private Scanner cli;
    private PrintStream printer;

    /**
     * Creates a new interface using the provided input and print streams
     * @param inputStream Stream to get input from
     * @param printStream Stream to print to
     */
    public CommandLineInterface(InputStream inputStream, PrintStream printStream) {
        cli = new Scanner(inputStream);
        printer = printStream;
    }

    public void setInputStream(InputStream inputStream) {
        cli = new Scanner(inputStream);
    }

    /**
     * Get the next value from the input stream
     * @return Next values from input stream as String
     */
    public String getNextLine() {
        return cli.nextLine();
    }

    /**
     * Print the string to the output stream
     * @param toPrint String to print
     */
    public void printLine(String toPrint) {
        printer.println(toPrint);
    }
}
