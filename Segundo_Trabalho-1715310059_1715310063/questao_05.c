#include<stdio.h>
#include<stdlib.h>
#include<string.h>


void DeletaComentarios(char *s){ 
     int Pos1, Pos2,i,tamanho;
     FILE *p, *Aux;
     char Linha[80];
     p = fopen(s, "rt");
     Aux = fopen("Temp.tmp", "wt");
     Tamanho = TamanhoArquivo(s);
     i = 0;
while (i < Tamanho){
    fgets(Linha, 80, p);
    i = i + strlen(Linha);
    Pos1 = Pos(Linha, "/*");
if (Pos1 != ­1){
    Pos2 = Pos(Linha, "*/");
if (Pos2 != ­1)
   DeletaCaracteres(Linha, Pos2, ­ Pos1 + 3, Pos1);
}
   fwrite(Linha, strlen(Linha), 1, Aux);
}
  fclose(p);
  
  fclose(Aux);
remove(s);
rename("Temp.tmp", s);
}


int main(){


    void DeletaComentarios(char *s);

    return 0;


}