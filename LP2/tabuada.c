#include <stdio.h>
#include <stdlib.h>

int tabuada(int n);

int main(){
    int n=10;

    tabuada(n);

    return 0;
}

int tabuada(int n){
    int i,j;

    for(j=2;j<=n;j++){
        for(i=1;i<=n;i++){

        printf("%d x %d = %d\n",i,j,i*j);

        }
        printf("\n");
    }
    return;
}
