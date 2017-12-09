#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

    char *nome;
    char *inverso;
    nome = malloc(10);
    inverso = malloc(10);

    printf("Digite uma palavra: \n");
    gets(nome);

    int i,igual=0,j=0;
    for(i=strlen(nome)-1;i>=0;i--){
    inverso[j]=nome[i];
    j++;
    }

    printf("\nInverso: %s\nlogo",inverso);

    for(i=0;i<strlen(nome);i++){
    if(nome[i]==inverso[i]) igual+=1;
    }

    if(igual==strlen(nome)) printf("\nÉ palindromo!\n");
    else printf("\nNão é palindromo!\n");

    free(nome);free(inverso);

    return 0;
}

