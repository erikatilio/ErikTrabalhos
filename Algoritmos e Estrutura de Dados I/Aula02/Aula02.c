#include <stdio.h>
#include <stdlib.h>

typedef struct{
  char nome[30];
  int idade;
  float coeficiente;
}tAluno;

int main(){
  tAluno *pAluno, aluno;
  pAluno = &aluno;

  puts("Informe o nome do aluno");
  gets(pAluno->nome);
  puts("Informe idade");
  scanf("%i",&pAluno->idade);
  puts("Informe o coeficiente");
  scanf("%f",&pAluno->coeficiente);

  printf("nome: %s\n",pAluno->nome);
  printf("idade: %i\n",pAluno->idade);
  printf("coeficiente: %.2f\n",pAluno->coeficiente);



  return 0;
}
