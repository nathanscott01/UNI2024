#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <math.h>
#include <pthread.h>

#define NUM_THREADS 8

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
void *integrateTrap(void *ptr)
{
	Worker *worker = (Worker*)ptr;


	double rangeSize = worker->rangeEnd - worker->rangeStart;
	double dx = rangeSize / worker->numSteps;
    double areax = 0;

	for (size_t i = 0; i < worker->numSteps; i++) {
		double smallx = worker->rangeStart + i*dx;
		double bigx = worker->rangeStart + (i+1)*dx;
        areax += dx * (worker->func(smallx) + worker->func(bigx) ) / 2;
	}

    pthread_mutex_lock(worker->lock);
    (*worker->area) += areax;
    pthread_mutex_unlock(worker->lock);

	return NULL;
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


int main(void)
{
	double rangeStart;
	double rangeEnd;
	size_t numSteps;
	MathFunc_t* func;
	char funcName[10] = {'\0'};

	pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
	Worker workers[NUM_THREADS];

	printf("Query format: [func] [start] [end] [numSteps]\n");


	while (getValidInput(&func, funcName, &rangeStart, &rangeEnd, &numSteps)) {
		double area = 0;

		// TODO
		// - Determine range and num_steps for each thread
		double rangeSize_t = (rangeEnd - rangeStart) / NUM_THREADS;
		double numSteps_t = numSteps / NUM_THREADS;

		// - Create a thread for each range
		for (size_t i = 0; i < NUM_THREADS; i++) {
			Worker *worker = &workers[i];
			worker->area = &area;
			worker->rangeStart = rangeStart + i * rangeSize_t;
			worker->rangeEnd = rangeStart + (i + 1) * rangeSize_t;
			worker->numSteps = numSteps_t;
			worker->func = func;

			worker->lock = &lock;
			pthread_create(&worker->thread, NULL, integrateTrap, (void*)worker);
		}

		// - Join the threads to area
		for (size_t i = 0; i < NUM_THREADS; i++) {
			pthread_join(workers[i].thread, NULL);
		}
		

		printf("The integral of function \"%s\" in range %g to %g is %.10g\n", funcName, rangeStart, rangeEnd, area);
	}

	_exit(0); // Forces more immediate exit than normal - **Use this to exit processes throughout the assignment!**
}
