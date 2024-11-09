#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define clear() printf("\033[H\033[J")
#define gotoxy(x,y) printf("\033[%d;%dH", (y), (x))

// ********************************

#ifdef WIN32
#include <windows.h>
#elif _POSIX_C_SOURCE >= 199309L
#include <time.h> // for nanosleep
#else
#include <unistd.h> // for usleep
#endif

void sleep_ms(int milliseconds)
{ // cross-platform sleep function
#ifdef WIN32
   Sleep(milliseconds);
#elif _POSIX_C_SOURCE >= 199309L
   struct timespec ts;
   ts.tv_sec = milliseconds / 1000;
   ts.tv_nsec = (milliseconds % 1000) * 1000000;
   nanosleep(&ts, NULL);
#else
   if (milliseconds >= 1000)
      sleep(milliseconds / 1000);
   usleep((milliseconds % 1000) * 1000);
#endif
}

int main(void) {
    int tamanho;
    int deltax = 20;                    //variaveis (delta x & y) para o retangulo ser impresso longe das letras
    int deltay = 10;
    // Lado 4
    for (tamanho = 1; tamanho <=20; tamanho++) {   //Define o tamanho da LINHA que será usado
        sleep_ms(50);                                   //Delay de 50 milisegundos anes de aparecer cada asterísco
        gotoxy(deltax + tamanho, deltay + 1);                                  //Coordenadas da LINHA (especificado a variavel delta, para afastar)
        printf("*");                                    //O jeito que essa linha será printada
        fflush(stdout);                                 //Comando para certificar que cada asterísco aparece individualmente (Para não carregar todos e daí aparecerem)
    }
    // Lado 3
    for (tamanho = 1; tamanho <= 10; tamanho++) {  //Define o tamanho de COLUNA que será usado
        sleep_ms(50);
        gotoxy(deltax + 20, deltay + tamanho);                                 //Coordenadas Da COLUNA mais da direita (especificado a variavel delta, para afastar)
        printf("*");
        fflush(stdout);    
    }
    // Lado 2
    for (tamanho = 20; tamanho >=1; tamanho--) {        //Fazer os mesmos desenhos porem de tras pra frente
        sleep_ms(50);
        gotoxy(deltax + tamanho, deltay + 10);
        printf("*");
        fflush(stdout);
    }
    //Lado 1
    for (tamanho = 10; tamanho >= 1; tamanho--) {
        sleep_ms(50);
        gotoxy(deltax + 1, deltay + tamanho);
        printf("*");
        fflush(stdout);
    }

    gotoxy (1,deltay + 11);                 //Para a mensagem no fim do código nao ficar em cima do retangulo 

    return 0;

}

//Para executa o código escreve 'gcc Retangulo.c -o Retangulo' (gcc + "seu codigo" -o + "nome de codigo" sem .c)
//Depois './ "Nome do código"'