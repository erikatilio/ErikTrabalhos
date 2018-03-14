#include <stdio.h>
#include <stdlib.h>

typedef struct{
  char nome[20] , matricula[10];
  float ap1 , ap2;
}tAluno;

void pedirDados(tAluno cadAlunos[]);
void mostrarDados(tAluno cadAlunos[]);

int main(){
  tAluno cadAlunos[5];

  pedirDados(cadAlunos);
  mostrarDados(cadAlunos);

  return 0;
}

void pedirDados(tAluno cadAlunos[]){
  for(int i=0;i<5;i++){
    printf("Digite o nome do aluno:\n");
    gets(cadAlunos[i].nome);
    printf("Digite a matricula:\n");
    gets(cadAlunos[i].matricula);

    printf("Digite usa AP1:\n");
    scanf("%d",&cadAlunos[i].ap1);
    printf("Digite usa AP2:\n");
    scanf("%d",&cadAlunos[i].ap2);
  }
}

void mostrarDados(tAluno cadAlunos[]){
  float maiorMedia = 0 , aux;

  for(int i=0;i<5;i++){
    printf("Nome: %s",cadAlunos[i].nome);
    printf("Matricula: %s",cadAlunos[i].matricula);
    aux = ((cadAlunos[i].ap1)+(cadAlunos[i].ap2))/2.0;
    if(aux > maiorMedia){
      maiorMedia = aux;
      printf("Media do Aluno: %.2f",aux);
    }else{
      printf("Media do Aluno: %.2f",aux);
    }
  }

  printf("Maior Media é %.2f",maiorMedia);
}
