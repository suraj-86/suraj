#include<stdio.h>
#include<string.h>

int main(){
    char a[]= "learn";
    char b[]= "about";
    char c[]= "string";
    char d[]= "variable";
    char e[]= "in";
    char f[]= "c program";

    char result[7];

    result[0]=c[3];
    result[1]=a[0];
    result[2]=b[2];
    result[3]=d[0];
    result[4]=d[strlen(d)-1];
    result[5]=b[strlen(b)-2];
    result[6]='\0';
    

    printf("%s\n",result);
}
