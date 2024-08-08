#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <stdbool.h>

bool testHandler(int sigNum, void (*func)(int)) {
    struct sigaction sa;
    if (sigaction(sigNum, NULL, &sa) == -1) {
        perror("sigaction");
        exit(0);
    }
    return sa.sa_handler == func;
}

void sampleHandler(int sig) {
    // Sample signal handler function
}

int main(void) {
    // Install the sampleHandler as the handler for SIGINT
    struct sigaction sa;
    sa.sa_handler = sampleHandler;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = 0;
    if (sigaction(SIGINT, &sa, NULL) == -1) {
        perror("sigaction");
        exit(EXIT_FAILURE);
    }

    // Test if the current handler for SIGINT is sampleHandler
    if (testHandler(SIGINT, sampleHandler)) {
        printf("The handler for SIGINT is sampleHandler\n");
    } else {
        printf("The handler for SIGINT is not sampleHandler\n");
    }

    return 0;
}
