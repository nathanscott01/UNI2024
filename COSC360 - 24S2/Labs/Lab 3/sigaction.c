#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <sys/types.h>  /* defines pid_t */
#include <unistd.h>	 /* defines fork() */
#include <sys/wait.h>   /* defines the wait() system call. */
#include <signal.h>

 /* Function prototypes */
void sighup(int sigNum); /* routines child will call upon sigtrap */
void sigint(int sigNum);
void sigquit(int sigNum);
void waitChild(int sigNum);


int main(void) {
	pid_t pid = 0;

    struct sigaction sa;    // Define sigaction struct

    // Setup sa to to handle SIGCHLD
    sa.sa_handler = waitChild;
    sigemptyset(&sa.sa_mask);
    sa.sa_flags = SA_RESTART;
    if (sigaction(SIGCHLD, &sa, NULL) == -1) {
        perror("sigaction");
        exit(1);
    }

	pid = fork();

	printf("pid is %i\n", pid);

	// Check for errors (we skip this in most examples, but you should always do it). 
	if (pid < 0) { 
		perror("fork"); // Print to stderr, "standard error". 
		exit(EXIT_FAILURE);

	} else if (pid == 0) {
		// Child code. 

		/* Register signal handlers. */
        // SIGHUP
        sa.sa_handler = sighup;
        sigemptyset(&sa.sa_mask);
        sa.sa_flags = SA_RESTART;
        if (sigaction(SIGHUP, &sa, NULL) == -1) {
            perror("sigaction");
            exit(1);
        }

        // SIGINT
        sa.sa_handler = sigint;
        if (sigaction(SIGINT, &sa, NULL) == -1) {
            perror("sigaction");
            exit(1);
        }

        // SIGQUIT
        sa.sa_handler = sigquit;
        if (sigaction(SIGQUIT, &sa, NULL) == -1) {
            perror("sigaction");
            exit(1);
        }

		while (true) {
			sleep(1); // Block forever. 
		}

	} else {
		// Parent code. 
		printf("Parent processing starts\n");

		printf("\nPARENT: sending SIGHUP\n\n");
		sleep(1); // Give the child some time to set up its signal handlers. 
		kill(pid, SIGHUP);
		sleep(3); // Pause for 3 seconds
		
		printf("\nPARENT: sending SIGINT\n\n");
		kill(pid, SIGINT);
		sleep(3); // Pause for 3 seconds. 
		
		printf("\nPARENT: sending SIGQUIT\n\n");
		kill(pid, SIGQUIT);
		
		printf("\nPARENT: Waiting for child to terminate...\n\n");
		while (true) {      // This keeps the parent responsive to signals
            pause();
        }
	}

	return EXIT_SUCCESS;
}

void sighup(int sigNum) {
	printf("CHILD: I have received a SIGHUP\n");
}

void sigint(int sigNum) {
	printf("CHILD: I have received a SIGINT\n");
}

void sigquit(int sigNum) {
	// We'll be exiting, so no need to reset signal in this case. 
	printf("CHILD: My DADDY has Killed me!!!\n");
	printf("CHILD: cleaning up...\n");
	sleep(2);
	exit(0);
}

void waitChild(int sigNum){
    // Wait when the parent recieves the SIGCHILD signal
    int childStatus;
    pid_t pid = wait(&childStatus);
    if (pid > 0) {
        printf("PARENT: Child with PID %d terminated with status %d\n", pid, childStatus);
        exit(0);
    } else {
        perror("wait");
    }
}