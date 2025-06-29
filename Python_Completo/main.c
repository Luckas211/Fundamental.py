#include <stdio.h>

char nome[50];
int idade;
float variavel1;
float variavel2;
int main()
{
  printf("numero 1: \n");
  scanf("%f", &variavel1);
  printf("numero 2: \n");
  scanf("%f", &variavel2);
  printf("%.2f", variavel1 + variavel2);
  
}