#include <stdio.h>
#include <math.h>
#include <string.h>

struct pokemom{
    char n[100];
    int l;
    int bs;
    int iv;
    int ev;
};

int main () {

    int t,i;
    scanf("%i",&t);

    struct pokemom jooj[t];

    for(i=0;i<t;i++){

    int hp, atk, def, sp;
    float aux;

    scanf("%s %i", &jooj[i].n, &jooj[i].l);
    //hp
    scanf ("%i %i %i", &jooj[i].bs, &jooj[i].iv, &jooj[i].ev);
    aux = sqrt(jooj[i].ev) / 8;
    hp = (((jooj[i].iv + jooj[i].bs + aux + 50) * jooj[i].l) / 50) + 10;

    //atk
    scanf ("%i %i %i", &jooj[i].bs, &jooj[i].iv, &jooj[i].ev);
    aux = sqrt(jooj[i].ev) / 8;
    atk = (((jooj[i].iv + jooj[i].bs + aux) * jooj[i].l) / 50) + 5;


    //def
    scanf ("%i %i %i", &jooj[i].bs, &jooj[i].iv, &jooj[i].ev);
    aux = sqrt(jooj[i].ev) / 8;
    def = (((jooj[i].iv + jooj[i].bs + aux) * jooj[i].l) / 50) + 5;


    //sp
    scanf ("%i %i %i", &jooj[i].bs, &jooj[i].iv, &jooj[i].ev);
    aux = sqrt(jooj[i].ev) / 8;
    sp = (((jooj[i].iv + jooj[i].bs + aux) * jooj[i].l) / 50) + 5;



    printf("Caso #%d: %s nivel %d\n", i+1, jooj[i].n, jooj[i].l);
    printf("HP: %d\n", hp);
    printf("AT: %d\n", atk);
    printf("DF: %d\n", def);
    printf("SP: %d\n", sp);
    }
    return 0;
}
