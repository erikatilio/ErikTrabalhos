#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

typedef struct{
	char nome[30];
	char end[40];
	char rg[10];
	char fone[12];
}tClientes;

int main(){
//criando arquivo
	FILE * arqClientes;
	tClientes vetCli[2], vetLeCli[2];
	int retorno;

	arqClientes = fopen("dadosCli.bin","w+");

//verificando abertura do arquivo
	if(arqClientes==NULL) cout << "\nErro na abertura do arquivo!" << endl;

//Escrevendo no arquivo
	for(int i=0;i<2;i++){
//nome
		puts("Nome ?");
		gets(vetCli[i].nome);
		printf("\n");

//endereço
		puts("Endereço ?");
		gets(vetCli[i].end);
		printf("\n");

//RG
		puts("RG ?");
		gets(vetCli[i].rg);
		printf("\n");

//fone
		puts("Telefone ?");
		gets(vetCli[i].fone);
		printf("\n");
	}

//gravando dados
	puts("[Gravando . . . .]");

	for(int i=0;i<2;i++){
		retorno = fwrite(&vetCli[i],sizeof(tClientes),1,arqClientes);
		if(retorno!=1) puts("Erro na Gravação do arquivo!!!");
		else puts("Gravado com sucesso!");
	}

//lendo dados
	rewind(arqClientes);

	puts("[Lendo . . . .]");

	for(int i=0;i<2;i++){
		retorno = fread(&vetLeCli[i],sizeof(tClientes),1,arqClientes);
		if(retorno!=1){
			if(feof(arqClientes)) break;
			puts("Erro na leitura");
		}
	}
//mostrando dados
	puts("[Mostrando dados . . . .]");

	for(int i = 0; i < 2; i++){
	printf("\nNome:			%s",vetLeCli[i].nome);
	printf("\nEndereco:		%s",vetLeCli[i].end);
	printf("\nFone:			%s",vetLeCli[i].fone);
	printf("\nRG:			%s\n",vetLeCli[i].rg);

}

	fclose(arqClientes);
  return 0;
}
