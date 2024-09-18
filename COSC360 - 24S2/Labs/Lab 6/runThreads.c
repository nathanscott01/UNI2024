#include <pthread.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>
#include <assert.h>

#define NUM_THREADS 5

bool hasRun[NUM_THREADS] = {false};

void runMe(int32_t *arg) {
    int32_t value = (*arg);
    assert(value >= 0 && value < NUM_THREADS && "Bad argument passed to 'runMe()!'");
    hasRun[value] = 1;
    int32_t *ret = (int32_t*)malloc(sizeof(int32_t));
    *ret = value * value;
    pthread_exit((void*)ret);
}

int32_t runThreads(size_t n) {
    pthread_t threads[n]; // Array to store thread IDs
    int32_t args[n];      // Arguments to pass to each thread
    int32_t sum = 0;      // Sum of the results

    // Create and start threads
    for (size_t i = 0; i < n; i++) {
        args[i] = i; // Set the argument to pass to the thread
        if (pthread_create(&threads[i], NULL, (void *(*)(void *))runMe, &args[i]) != 0) {
            perror("Failed to create thread");
            exit(1);
        }
    }

    // Wait for all threads to finish and collect their results
    for (size_t i = 0; i < n; i++) {
        int32_t *result;
        if (pthread_join(threads[i], (void **)&result) != 0) {
            perror("Failed to join thread");
            exit(1);
        }

        sum += *result; // Sum up the results
        free(result);   // Free the allocated memory
    }
    return sum;
}

int main (void) {
    int32_t sum = runThreads(NUM_THREADS);
    size_t numCorrect = 0;
    for (size_t i = 0; i < NUM_THREADS; i++) {
        if (hasRun[i]) {
            numCorrect++;
        }
    }
    printf("%zu %d\n", numCorrect, sum);
    return 0;
}