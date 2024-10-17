PTHREAD_LIB = -lpthread
CC = gcc
CFLAGS = -g -Wall -Werror -lm

.PHONY: default all clean

all: serial thread process proc_thread run_time proc_thread_input run_time_procthread

serial: serial.c
	@$(CC) serial.c -o serial $(CFLAGS)

thread: thread.c
	@$(CC) thread.c -o thread $(CFLAGS) $(PTHREAD_LIB)

process: process.c
	@$(CC) process.c -o process $(CFLAGS)

proc_thread: processThread.c
	@$(CC) processThread.c -o proc_thread $(CFLAGS) $(PTHREAD_LIB)

proc_thread_input: processThread_input.c
	@$(CC) processThread_input.c -o proc_thread_input $(CFLAGS) $(PTHREAD_LIB)

run_time: run_timing.c
	@$(CC) run_timing.c -o run_time $(CFLAGS)

run_time_procthread: run_timing_procthread.c
	@$(CC) run_timing_procthread.c -o run_time_procthread $(CFLAGS)

clean:
	@-rm -f *.o
	@-rm -f serial thread process proc_thread run_time proc_thread_input run_time_procthread