#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x, y;
    printf("Enter two numbers: ");
    scanf_s("%d %d", &x, &y);

    swap(&x, &y);
    printf("After swapping: %d %d\n", x, y);
    return 0;
}
