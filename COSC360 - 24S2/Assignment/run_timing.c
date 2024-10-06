#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_FILES 4
#define NUM_TEST_CASES 6

// Filenames for executables and input sizes
char *files[] = { "./serial", "./thread", "./process", "./proc_thread" };
char *inputFiles[] = { "input_5.txt", "input_10.txt", "input_20.txt", "input_30.txt", "input_40.txt", "input_50.txt" };

// Run the time command on each file for each input
void run_timing() {
    char command[256];  // Buffer for system commands
    
    FILE *outputFile = fopen("results.txt", "w");

    if (outputFile == NULL) {
        perror("Unable to open results.txt");
        exit(1);
    }

    for (int i = 0; i < NUM_FILES; i++) {
        for (int j = 0; j < NUM_TEST_CASES; j++) {
            snprintf(command, sizeof(command), "echo 'Running %s with %s' >> results.txt", files[i], inputFiles[j]);
            system(command);

            // Format: time command output to results.txt, redirecting both stdout and stderr
            snprintf(command, sizeof(command), "(/usr/bin/time -p %s < %s) >> results.txt 2>&1", files[i], inputFiles[j]);
            system(command);

            // Adding a separator between runs for clarity
            system("echo '---------------------------------' >> results.txt");
        }
    }

    fclose(outputFile);
}

int main(void) {
    run_timing();
    return 0;
}
