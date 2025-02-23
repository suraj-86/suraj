#include<stdio.h>
int main(){
    int a[5]={10,20,30,40,50},n,found=0;
    printf("enter no:");
    scanf("%d",&n);
    int count=0;

    for(int i=0;i<5;i++){
        if(a[i]==n){
            found=1;
            break;
        }   
        count ++;
    }
    if(found)
        printf("%d found in array at index %d",n,count);
    else
        printf("%d not found in array",n);
    return 0;

}