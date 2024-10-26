#include <stdio.h>
#include <math.h>

int main() {
    //1º passo: identificação das grandezas (as que nos ja sabemos não mudam, apenas as que podem variar)
    printf("Qual a quantidade de pintores? ");
    float p;
    scanf("%f", &p);                               //NOTA: 4 pintores(p) pintarem 6 escolas(e) em 8 dias(d) é a certeza
    printf("Quantas escolas eles irão pintar? ");
    float e;
    scanf("%f", &e);
    //2 passo: montar a equação, isolar a incógnia e multiplicar o inverso do (inversamente proporcional) pelo diretamente proporcional
    float d = (16*e)/(3*p);                        //(8/x = p/4 . 6/e)
    printf("Vai levar %f dias\n", d);

    return 0;

}