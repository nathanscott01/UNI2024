#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>


#define HANDLE_ERROR(msg) \
	do { perror(msg); exit(EXIT_FAILURE); } while (0)

size_t fileSize(int fd) {
	struct stat sb;	
	if (fstat(fd, &sb) == -1) HANDLE_ERROR("fstat");
	
	return	sb.st_size;
}


int main(int argc, char *argv[])
{
	char *addr1;
	char *addr2;
	
	if (argc < 2) {
		fprintf(stderr, "usage: %s <repeats>\n", argv[0]);
		exit(EXIT_FAILURE);
	}

	size_t repeats = atoi(argv[1]);
	

	for (uint32_t i = 0; i < repeats; ++i) {

		int src = open("test.dat", O_RDONLY);
		if (src == -1) {
			printf("Success\n");
			HANDLE_ERROR("fstat");
		}

		int dst = open("output.dat", O_RDWR | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
		if (dst == -1) {
			HANDLE_ERROR("open");
		}

		// get the file size	
		size_t size = fileSize(src);
		
		// Need to truncate the file to the right size or mmap will fail
		if (ftruncate(dst, size)) {
			HANDLE_ERROR("ftruncate");
		}

		
		/*
		 * TODO: Implement file copying using mmap.
		 * 
		 * First, mmap both the files to a region of memory.
		 * Copy the contents between the memory regions using memcpy.
		 * Use munmap to unmap the files and make sure the data is written
		 * 
		 * MAP_PRIVATE for reading the source	because we don't need to propogate writes to the file	 
		 * We need MAP_SHARED on the destination so that our writes are written back to the file
		 * 
		 */

		// Map both files to memory
		addr1 = mmap(NULL, size, PROT_READ, MAP_PRIVATE, src, 0);
		if (addr1 == MAP_FAILED) {
			HANDLE_ERROR("mmap src");
		}

		addr2 = mmap(NULL, size, PROT_WRITE, MAP_SHARED, dst, 0);
		if (addr2 == MAP_FAILED) {
			HANDLE_ERROR("mmap dst");
		}

		// Copy contents
		memcpy(addr2, addr1, size);

		// Unmap files
		if (munmap(addr1, size) == -1) {
			HANDLE_ERROR("munmap src");
		}

		if (munmap(addr2, size) == -1) {
			HANDLE_ERROR("munmap dest");
		}

		close(src);
		close(dst);
	}

	exit(EXIT_SUCCESS);
}