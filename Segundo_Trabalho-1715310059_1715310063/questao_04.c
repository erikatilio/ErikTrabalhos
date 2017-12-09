#include <stdlib.h>
#include <stdio.h>

int main() {
  char nome[40];
  int i = 0, t = 0, fpn = 0, spc = 0, vspc[10], k = 0;
  fgets(nome,40,stdin);
  while ( nome[i] != '\n' ){
    if ( nome[i] == ' '){
      vspc[k] = i+1;
      
      k++;
      spc++;
    }
    
    t++; 
    
    i++;
  }

    for(i=vspc[k-1];i<t;i++)
    {
      printf("%c", nome[i]);
    }

    printf("/");

    fpn = vspc[0] - 1; 

    for(i=0;i<fpn;i++){
      printf("%c", nome[i]);
        
    }
    printf("\n");
	return 0;
}