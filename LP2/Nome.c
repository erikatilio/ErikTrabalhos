#include <stdio.h>
#include <stdlib.h>

int main(){
    char *nome;register i;
    nome = (char *)malloc(10*sizeof(char));

    printf("Digite seu nome: ");
    gets(nome);

    for(i=strlen(nome); i>=0;i--){
        printf("%c",nome[i]);
    }

    free(nome);


    return 0;
}
