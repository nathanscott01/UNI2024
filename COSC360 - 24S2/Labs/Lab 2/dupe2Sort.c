#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(void) {

    int fd;

    /* Open my.file */
    if ((fd = open("my.file", O_RDONLY)) == -1) {
        perror("Couldn't open my.file");
        exit(1);
    }

    /* Redirect stdout to my.file */
    if (dup2(STDOUT_FILENO, fd) == -1) {
        perror("Could not redirect stdout");
        exit(2);
    }

    /* Replace the current process with "sort -k +7" */
    execl("/bin/sort", "sort", "-k", "+7", NULL);

    /* If we reach this line, execl must have failed */
    perror("Exec failed");
    exit(3);
}
