#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <assert.h>


typedef struct {
	char *data;
	
	size_t length;
	size_t reserved;
} Buffer;


/*
 * Create a new buffer, reserving an initial amount of memory
 * length starts at zero.
 */
Buffer *newBuffer(size_t reserved) {
	/* TODO */
	Buffer *buffer = malloc(sizeof(Buffer));
	if (buffer == NULL) {
		perror("Failed to allocate space for buffer");
		exit(EXIT_FAILURE);
	}

	buffer->data = malloc(reserved);
	if (buffer->data == NULL) {
		free(buffer);
		perror("Failed to allocate space for data");
		exit(EXIT_FAILURE);
	}

	buffer->length = 0;
	buffer->reserved = reserved;

	return buffer;
}


void freeBuffer(Buffer *buffer) {
	free(buffer->data);
	free(buffer);
}


/*
 * Append data to a buffer.
 * 
 * If the reserved amount is not enough to fit the buffer,
 * double the reserved amount and try again (until it fits).
 * 
 * Finally, append the data to the end of the buffer and increase it's length.
 */
void appendBuffer(Buffer *buffer, char *data, size_t length) {
	/* TODO */
	while (buffer->length + length > buffer->reserved) {
		buffer->reserved *= 2;
		char *new_data = realloc(buffer->data, buffer->reserved);
		if (new_data == NULL) {
            perror("Failed to reallocate space for buffer data");
            exit(EXIT_FAILURE);
        }
        buffer->data = new_data;
	}
	memcpy(buffer->data + buffer->length, data, length);
	buffer->length += length;
}




int main(int argc, char *argv[])
{
	if (argc < 2) {
		fprintf(stderr, "usage: %s <repeats>\n", argv[0]);
		exit(EXIT_FAILURE);
	}
	
	size_t repeats = atoi(argv[1]);
	size_t chunk_size = 1024;
	
	for (uint32_t i = 0; i < repeats; ++i) {
	
		FILE *src = fopen("test.dat", "r");
		if (src == NULL) {
			fprintf(stderr, "error opening test.dat");
			exit(EXIT_FAILURE);
		}

		FILE *dst = fopen("output.dat", "w");
		if (dst == NULL) {
			fprintf(stderr, "error opening output.dat");
			exit(EXIT_FAILURE);
		}
		
		
		char *data = malloc(chunk_size);
		Buffer *buffer = newBuffer(chunk_size);
		
		size_t bytes = 0;
		while ((bytes = fread(data, 1, chunk_size, src)) > 0) {
			appendBuffer(buffer, data, bytes);
		}
		
		fwrite(buffer->data, buffer->length, 1, dst);
		
		fclose(src);
		fclose(dst);
		
		free(data);
		freeBuffer(buffer);
	}
	
	exit(EXIT_SUCCESS);
}