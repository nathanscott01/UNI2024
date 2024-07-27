#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

#define INP 1
#define OUTP 0

int main(void) {
    int fd[2];
    pid_t childpid;

    pipe(fd);
    if ((childpid = fork()) == 0) { /* Child code: Runs ls */
        dup2(fd[INP], STDOUT_FILENO);
        close(fd[OUTP]);
        close(fd[INP]);
        char *args[] = {"sort", "-k", "+1", NULL};
        execvp("sort", args);        
        perror("The exec of sort failed");
    }

    else { /* Parent code: Runs sort */
        dup2(fd[OUTP], STDIN_FILENO);
        close(fd[OUTP]);
        close(fd[INP]);
        char *args[] = {"head", "-2", NULL};
        execvp("head", args);
        /* Note: The location of sort depends on your distribution.
         * Use 'which sort' to find the correct location */
        perror("The exec of head failed");
    }

    exit(0);
}
