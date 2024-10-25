#include <stdio.h>
#include <math.h>

int main() {
    //Pegar um valor (a)
    printf("Digite um valor (1/3) ");
    float a;
    scanf("%f", &a);
    //Pegar um valor (b)
    printf("Digite um valor (2/3) ");
    float b;
    scanf("%f", &b);
    //pegar um valor (c)
    printf("Digite um valor (3/3) ");
    float c;
    scanf("%f", &c);
    //Cálculo de Delta
    float d = (pow(b,2)-(4*a*c)); // b elevado a 2, menos 4 vezes a vezes c

    printf("delta = %f \n", d);
    // Se delta for menor que 0
    if (d < 0) {
        // Mostrar que nao existe raiz
        printf ("Delta não tem raíz");
    }
    // senão se delta for igual a 0
    else if (d == 0) {
        // Calcula a raiz (-b / 2a)
        float umaraiz;
        umaraiz = (-b / (2*a));
        // Mostar que tem uma raiz
        printf("A raiz é %.2f\n",umaraiz);
    }
    //Senão se delta for maior que 0
    else {  
        //calcula a raiz (-b + (delta)/2a)
        float raizmais;
        raizmais = ((-b + sqrt(d))/ (2*a));
        // calcula a raiz (-b - (delta)/2a)
        float raizmenos;
        raizmenos = ((-b - sqrt(d))/ (2*a));
        // mostrar as duas raizes
        printf("As raizes são %f e %f \n",raizmais,raizmenos);
    }

    return 0;
}