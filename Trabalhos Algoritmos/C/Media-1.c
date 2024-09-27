#include <stdio.h>
#include <math.h>
 
int main() {
    float a;
    scanf("%f", &a);
    a = a * 3.5;
    float b;
    scanf("%f", &b);
    b = b * 7.5;
    printf("MEDIA = %.5lf\n", (a + b)/11);
    return 0;
}