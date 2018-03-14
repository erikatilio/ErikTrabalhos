#include <stdio.h>
#include <stdlib.h>

typedef struct{
  char nVoo[10] , tipo[10];
  float preco;
  int lugares;
}tAviao;

int main(){
  tAviao voos[10];
  float menorPreco , maiorPreco;

  for(int i=0;i<10;i++){
    printf("%i Voo\n",i+1);
    puts("Numero do Voo: ");
    gets(voos[i].nVoo);
    puts("Tipo: ");
    gets(voos[i].tipo);
    puts("Preço: ");
    scanf("%f",&voos[i].preco);
    puts("Lugares: ");
    scanf("%i",&voos[i].lugares);
    printf("\n");
  }

  printf("Qual o menor e o maior preço que deseja pagar???\n");
  scanf("%f%f",&menorPreco,&maiorPreco);

  for(int i=0;i<10;i++){
    if(voos[i].preco >= menorPreco && voos[i].preco <= maiorPreco){
      printf("Numero de Voo:    %s",voos[i].nVoo);
      printf("Tipo:    %s",voos[i].tipo);
      printf("Preço:    %.2f",voos[i].preco);
      printf("Lugares:    %i",voos[i].lugares);
    }
  }

  return 0;
}
