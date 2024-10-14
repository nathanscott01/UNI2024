#include <stdio.h>
#include <stdlib.h>

void run_timing() {
    char command[256];  // Buffer for system commands
    int children[] = {3, 6, 9};
    int threads[] = {4, 8, 16};
    const char *inputFile = "input_10.txt";
    const char *file = "./procthread_input";  // Adjusted to only test this executable
    
    FILE *outputFile = fopen("procthread_results.txt", "w");
    if (outputFile == NULL) {
        perror("Unable to open procthread_results.txt");
        exit(1);
    }

    // Loop over all combinations of children and threads
    for (int i = 0; i < sizeof(children) / sizeof(children[0]); i++) {
        for (int j = 0; j < sizeof(threads) / sizeof(threads[0]); j++) {
            // Print the header line with the current combination
            snprintf(command, sizeof(command),
                     "echo 'Running %s with %s, n_child = %d, n_thread = %d' >> procthread_results.txt",
                     file, inputFile, children[i], threads[j]);
            system(command);

            // Run the time command with the current parameters, redirecting both stdout and stderr
            snprintf(command, sizeof(command),
                     "(/usr/bin/time -p %s %d %d < %s) >> procthread_results.txt 2>&1",
                     file, children[i], threads[j], inputFile);
            system(command);

            // Add a separator for clarity between runs
            system("echo '---------------------------------' >> procthread_results.txt");
        }
    }

    fclose(outputFile);
}

int main(void) {
    run_timing();
    return 0;
}
