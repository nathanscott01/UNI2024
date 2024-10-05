#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <math.h>
#include <semaphore.h>
#include <signal.h>
#include <sys/wait.h>

#define MAX_CHILDREN 3

static sem_t numFreeChildren;
typedef double MathFunc_t(double);


double gaussian(double x)
{
	return exp(-(x*x)/2) / (sqrt(2 * M_PI));
}


double chargeDecay(double x)
{
	if (x < 0) {
		return 0;
	} else if (x < 1) {
		return 1 - exp(-5*x);
	} else {
		return exp(-(x-1));
	}
}


// Integrate using the trapezoid method. 
double integrateTrap(MathFunc_t* func, double rangeStart, double rangeEnd, size_t numSteps)
{
	double rangeSize = rangeEnd - rangeStart;
	double dx = rangeSize / numSteps;

	double area = 0;
	for (size_t i = 0; i < numSteps; i++) {
		double smallx = rangeStart + i*dx;
		double bigx = rangeStart + (i+1)*dx;

		area += dx * ( func(smallx) + func(bigx) ) / 2; // Would be more efficient to multiply area by dx once at the end. 
	}

	return area;
}


bool getValidInput(MathFunc_t** func, char* funcName, double* start, double* end, size_t* numSteps)
{
	memset(funcName, '\0', 10); // Clear funcName. Magic number used because format strings are annoying. 

	// Read input numbers and place them in the given addresses:
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

	// Return whether the given func and range is valid:
	return (numRead == 4 && *func != NULL && *end >= *start && *numSteps > 0);
}


void waitChild(int childNum) {
    int childStatus;
    while (waitpid(-1, &childStatus, WNOHANG) > 0) {
        sem_post(&numFreeChildren);
    }
}


int main(void)
{
	double rangeStart;
	double rangeEnd;
	size_t numSteps;
	MathFunc_t* func;
	char funcName[10] = {'\0'};

    sem_init(&numFreeChildren, 0, MAX_CHILDREN);

    struct sigaction sa;
    sa.sa_handler = waitChild;
    sa.sa_flags = SA_RESTART;
    sigaction(SIGCHLD, &sa, NULL);

	printf("Query format: [func] [start] [end] [numSteps]\n");

    while (getValidInput(&func, funcName, &rangeStart, &rangeEnd, &numSteps)) {

        sem_wait(&numFreeChildren);

        pid_t pid = fork();

        if (pid < 0) {
            perror("Fork");
            exit(EXIT_FAILURE);
        } else if (pid == 0) {
            double area = integrateTrap(func, rangeStart, rangeEnd, numSteps);
            printf("Child (PID %d): The integral of function \"%s\" in range %g to %g with %ld steps is %.10g\n", getpid(), funcName, rangeStart, rangeEnd, numSteps, area);
        }

    }

	_exit(0); // Forces more immediate exit than normal - **Use this to exit processes throughout the assignment!**
}
