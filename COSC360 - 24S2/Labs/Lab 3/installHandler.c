#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>

static int sigquit_count = 0;

void sigquit_handler(int sig) {
    sigquit_count++;
    write(1, "SIGQUIT\n", 8);

    if (sigquit_count == 1) {
        signal(SIGQUIT, sigquit_handler);
    } else if (sigquit_count == 2) {
        exit(0);
    }
}

void installHandler(void) {
    signal(SIGQUIT, sigquit_handler);
}

