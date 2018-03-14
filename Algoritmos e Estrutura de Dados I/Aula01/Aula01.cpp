#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>

using namespace std;

int main(){
	FILE *arquivo;
	arquivo = fopen("arquivo.txt","r");

//Verfificar abertura
	if(arquivo == NULL) cout << "O Arq. não pôde ser aberto!\n";
	else cout << "Arq. aberto com sucesso!\n\n";

/*
//Gravando dados
	fprintf(arquivo,"%d %d %s", 12,12,"maria\n");
	fprintf(arquivo,"%d %d %s", 222,32,"joao\n");
*/

//Lendo dados
	int n1 , n2;
	char nome[30];

	while((fscanf(arquivo,"%d %d %s\n", &n1, &n2, nome))!=EOF ){
		cout << nome << " ";
		cout << n1 << " ";
		cout << n2 << endl;
	}

	fclose(arquivo);
  return 0;
}
