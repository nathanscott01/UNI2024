/*
 * numSort.c - A mostly empty file. Write a program that sorts an array of numbers (the type doesn't really matter) using the library function qsort().
 */

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Comparing function used by qsort
int32_t compare(const void* a, const void* b) {
  return(*(int*)a - *(int*)b);
}

// Function containing qsort
int main() {
  size_t n = 7;
  int32_t data[] = {1, 5, 2, 7, 4, 8, 3};
  // Expected: [1, 2, 3, 4, 5, 7, 8]
  qsort(data, n, sizeof(int32_t), compare);
  for (int i = 0; i < n; i++) {
    printf("%d ", data[i]);
  }
  printf("\n");
  return 0;
}
