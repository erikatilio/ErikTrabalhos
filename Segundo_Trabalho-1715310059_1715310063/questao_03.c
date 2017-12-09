#include <stdio.h>
#include <string.h>

int main(){
    char frase[40],esc[10],sub[10];

    gets(frase);

    gets(esc);
    char *antes = strstr(frase,esc);
    gets(sub);

    int i,tam=strlen(antes),cont=0;

    for(i=0;i<tam;i++){
        if(antes[i]== ' ') break;
        cont++;
        }
    char aux[20];aux[0]=' ';
    int j=1;
    for(i=0;i<tam;i++) if(i>cont)aux[j]=antes[i], j++;

    char auy[20];

    for(i=0;i<(strlen(frase) - tam);i++) auy[i]=frase[i];

    char *part1 = strcat(auy,sub);
    char *part2 = strcat(part1,aux);
    printf("%s\n",part2);

    return 0;
}
