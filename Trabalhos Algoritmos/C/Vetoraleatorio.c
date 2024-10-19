#include <stdio.h>

int main() {
    //Iniciar vetor
    int tam = 10;
    int v[tam];
    int j = 0;
    int n = 0;
    //repete enquanto não houver 10 elementos no vetor
    while (j < tam) {

        //Escolhe um numero aleatorio
        printf("Digite um numero");
        scanf("%d", &n);

        // -------------- Se x não estiver no vetor

        // crie uma flag dizendo que não encontrou
        int dentro = 0;
        // percorre o vetor
        for (int i = 0; i < j; i++){
            // o numero atual é o mesmo que o procurado? achamos ele?
            if (v[i]== n){
                // sinaliza que encontrou
                dentro = 1;
                // interrompe busca
                break;
            }
        }
            // adiciona o x no vetor
            if (dentro == 0) {
                v[j] = n;
                j++;
            }

    }
    // Mostre os valores do vetor
     for (int i = 0; i < tam; i++){
        printf("%d\n", v[i]);
     }
}