#include<stdio.h>
int main(){
    int a[5]={10,20,30,40,50},sum=0;
    for(int i=0;i<5;i++){
        sum+=a[i];
    }
    printf("average is:%d",sum/5);
}