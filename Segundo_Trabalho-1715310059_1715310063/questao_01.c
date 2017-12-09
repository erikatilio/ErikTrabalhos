#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
   FILE *doc;
   doc = fopen("Notas.txt","r");
   char linha[100],nome[20],sobrenome[20],bos[20];
   float media=0,nota=0;
   int aux=0;


  while(fgets(linha,100,doc)!=NULL){
        if(sscanf(linha,"%s %s %f",nome,sobrenome,&nota) == 1){
            printf("%s %s %.1f\n",nome,sobrenome,nota);
            media += nota;
            aux+= 1;
        }else{
            sscanf(linha,"%s %s %s %f",nome,sobrenome,bos,&nota);
            printf("%s %s %.1f\n",nome,sobrenome,bos,nota);
            media += nota;
            aux+= 1;
        }
    }
    media = media/aux;

    printf("Media: %.2f",media);


   fclose(doc);

   return 0;
}

