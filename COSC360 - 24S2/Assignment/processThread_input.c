#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <math.h>
#include <pthread.h>
#include <semaphore.h>
#include <signal.h>
#include <sys/wait.h>

// No longer using fixed #defines for MAX_CHILDREN and NUM_THREADS
static sem_t numFreeChildren;
typedef double MathFunc_t(double);

typedef struct {
    double *area;
    double rangeStart;
    double rangeEnd;
    size_t numSteps;
    MathFunc_t* func;

    pthread_mutex_t *lock;
    pthread_t thread;
} Worker;

// Mathematical functions
double gaussian(double x) {
    return exp(-(x * x) / 2) / (sqrt(2 * M_PI));
}

double chargeDecay(double x) {
    if (x < 0) {
        return 0;
    } else if (x < 1) {
        return 1 - exp(-5 * x);
    } else {
        return exp(-(x - 1));
    }
}

// Thread function for integration using the trapezoid method
void *integrateTrap(void *ptr) {
    Worker *worker = (Worker*)ptr;
    double rangeSize = worker->rangeEnd - worker->rangeStart;
    double dx = rangeSize / worker->numSteps;
    double local_area = 0;

    for (size_t i = 0; i < worker->numSteps; i++) {
        double smallx = worker->rangeStart + i * dx;
        double bigx = worker->rangeStart + (i + 1) * dx;
        local_area += dx * (worker->func(smallx) + worker->func(bigx)) / 2;
    }

    // Protect access to the shared area variable
    pthread_mutex_lock(worker->lock);
    *(worker->area) += local_area;
    pthread_mutex_unlock(worker->lock);

    return NULL;
}

bool getValidInput(MathFunc_t** func, char* funcName, double* start, double* end, size_t* numSteps) {
    memset(funcName, '\0', 10); // Clear funcName
    size_t numRead = scanf("%9s %lf %lf %zu", funcName, start, end, numSteps);

    if (strcmp(funcName, "sin") == 0) {
        *func = &sin;
    } else if (strcmp(funcName, "gauss") == 0) {
        *func = &gaussian;
    } else if (strcmp(funcName, "decay") == 0) {
        *func = &chargeDecay;
    } else {
        *func = NULL;
    }

    return (numRead == 4 && *func != NULL && *end >= *start && *numSteps > 0);
}

// Signal handler for cleaning up child processes
void waitChild(int childNum) {
    int childStatus;
    while (waitpid(-1, &childStatus, WNOHANG) > 0) {
        sem_post(&numFreeChildren);
    }
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <number_of_children> <number_of_threads>\n", argv[0]);
        return 1;
    }

    // Parse command-line arguments for the number of children and threads
    int maxChildren = atoi(argv[1]);
    int numThreads = atoi(argv[2]);

    if (maxChildren <= 0 || numThreads <= 0) {
        fprintf(stderr, "Error: Number of children and threads must be positive integers.\n");
        return 1;
    }

    // Initialize the semaphore with the number of child processes
    sem_init(&numFreeChildren, 0, maxChildren);
    signal(SIGCHLD, waitChild);

    double rangeStart, rangeEnd;
    size_t numSteps;
    MathFunc_t* func;
    char funcName[10] = {'\0'};
    pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
    Worker *workers = malloc(numThreads * sizeof(Worker));

    printf("Query format: [func] [start] [end] [numSteps]\n");

    while (getValidInput(&func, funcName, &rangeStart, &rangeEnd, &numSteps)) {
        sem_wait(&numFreeChildren);
        pid_t pid = fork();

        if (pid < 0) {
            perror("Fork");
            exit(EXIT_FAILURE);
        } else if (pid == 0) {
            double area = 0;
            double rangeSizePerThread = (rangeEnd - rangeStart) / numThreads;
            size_t numStepsPerThread = numSteps / numThreads;

            // Create threads for the child process
            for (size_t i = 0; i < numThreads; i++) {
                Worker *worker = &workers[i];
                worker->area = &area;
                worker->rangeStart = rangeStart + i * rangeSizePerThread;
                worker->rangeEnd = rangeStart + (i + 1) * rangeSizePerThread;
                worker->numSteps = numStepsPerThread;
                worker->func = func;
                worker->lock = &lock;
                pthread_create(&worker->thread, NULL, integrateTrap, (void*)worker);
            }

            // Join threads
            for (size_t i = 0; i < numThreads; i++) {
                pthread_join(workers[i].thread, NULL);
            }

            printf("Child (PID %d): The integral of function \"%s\" in range %g to %g is %.10g\n",
                   getpid(), funcName, rangeStart, rangeEnd, area);
            _exit(0);
        }
    }

    // Wait for all child processes to finish
    while (wait(NULL) > 0);

    free(workers);
    sem_destroy(&numFreeChildren);
    return 0;
}