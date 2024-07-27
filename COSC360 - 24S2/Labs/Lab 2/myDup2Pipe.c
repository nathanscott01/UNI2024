#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

#define INP 1
#define OUTP 0

int main(void) {
    int fd1[2], fd2[2];             // Pipe
    pid_t child1pid, child2pid;     // Children

    if (pipe(fd1) == -1) {
        perror("Pipe 1");
        exit(1);
    }
    if (pipe(fd2) == -1) {
        perror("Pipe 2");
        exit(1);
    }


    if ((child1pid = fork()) == 0) {        /* Child 1 - Runs ls -l */
        dup2(fd1[INP], STDOUT_FILENO);      // Plumb the output into pipe 1
        close(fd1[OUTP]);
        close(fd1[INP]);
        close(fd2[OUTP]);
        close(fd2[INP]);
        execl("/bin/ls", "ls", "-l", NULL);
        perror("The exec of ls failed");
        exit(2);
    } else if ((child2pid = fork() == 0)) { /* Child 2 - Runs sort -k +9 */
        dup2(fd1[OUTP], STDIN_FILENO);      // Plumb output of pipe 1 to input
        dup2(fd2[INP], STDOUT_FILENO);      // Plumb std output into pipe 2
        close(fd1[OUTP]);
        close(fd1[INP]);
        close(fd2[OUTP]);
        close(fd2[INP]);
        execl("/bin/sort", "sort", "-k", "+9", NULL);
        perror("The exec of sort failed");
        exit(3);
    } else {                                /* Parent code - Runs head -5 */
        dup2(fd2[OUTP], STDIN_FILENO);      // Plumb output of pipe 2 to input
        close(fd1[OUTP]);
        close(fd1[INP]);
        close(fd2[OUTP]);
        close(fd2[INP]);
        execl("/usr/bin/head", "head", "-5", NULL);
        /* Note: The location of sort depends on your distribution.
         * Use 'which sort' to find the correct location */
        perror("The exec of head failed");
        exit(4);
    }

    exit(0);
}
