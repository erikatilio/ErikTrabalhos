#include <stdio.h>
#include <stdlib.h>

typedef struct{
  char rua[20] , bairro[20] , cidade[10] , estado[10] , cep[20];
}tEndereco;

typedef struct{
  char nome[30], identidade[20] , cpf[20] , estadoCivil[10] , telefone[10];
   char idade[4], sexo[1] , salario[10];
  tEndereco endereco;
}tCadastro;

int main(){
  tCadastro vetCad[2];
  char busca[20];

  for(int i=0;i<2;i++){
    puts("Nome?: ");
    gets(vetCad[i].nome);
    
    puts(" ");
    puts("Endereço:");
    puts("Rua?: ");
    gets(vetCad[i].endereco.rua);
    puts("Bairro?: ");
    gets(vetCad[i].endereco.bairro);
    puts("Cidade?: ");
    gets(vetCad[i].endereco.cidade);
    puts("Estado?: ");
    gets(vetCad[i].endereco.estado);
    puts("Cep?: ");
    gets(vetCad[i].endereco.cep);
    puts(" ");

    puts("Salário?: ");
    gets(vetCad[i].salario);
    puts("Identidade?: ");
    gets(vetCad[i].identidade);
    puts("CPF?: ");
    gets(vetCad[i].cpf);
    puts("Estado Civil?: ");
    gets(vetCad[i].estadoCivil);
    puts("Telefone:? ");
    gets(vetCad[i].telefone);
    puts("Idade?: ");
    gets(vetCad[i].idade);
    puts("Sexo?(M-masculino/F-feminino):");
    gets(vetCad[i].sexo);
    puts(" ");
}

for(int i=0;i<2;i++){
    puts("Dados do Cliente");
    printf("Nome:   %s\n\n",vetCad[i].nome);
    printf("Salário:    %s\n",vetCad[i].salario);
    printf("Identidade:   %s\n",vetCad[i].identidade);
    printf("CPF:    %s\n",vetCad[i].cpf);
    printf("Estado Civil:   %s\n",vetCad[i].estadoCivil);
    printf("Telefone:   %s\n",vetCad[i].telefone);
    printf("Idade:    %s\n",vetCad[i].idade);
    printf("Sexo:   %s\n\n",vetCad[i].sexo);

    printf("Endereço:\n");
    printf("Rua:   %s\n",vetCad[i].endereco.rua);
    printf("Bairro:   %s\n",vetCad[i].endereco.bairro);
    printf("Cidade:   %s\n",vetCad[i].endereco.cidade);
    printf("Estado:   %s\n",vetCad[i].endereco.estado);
    printf("CEP:    %s\n\n",vetCad[i].endereco.cep);
}



  return 0;
}
