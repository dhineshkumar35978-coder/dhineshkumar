#include <stdio.h>

// Engineered function to add n numbers
int add_numbers(const int *arr, int n) {
    int sum = 0;                   // 1. Initialize accumulator
    for (int i = 0; i < n; i++) {  // 2. Iterate over all elements
        sum = sum + arr[i];        // 3. Add current element
    }
    return sum;                    // 4. Return final result
}

int main(void) {
    int values[] = {10, 20, 30, 40};
    int n = sizeof(values) / sizeof(values[0]);

    int result = add_numbers(values, n);
    printf("Sum = %d\n", result);

    return 0;
}
