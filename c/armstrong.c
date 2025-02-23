#include<stdio.h>
int power(int a ,int b){
    int result=1;
    for(int i=0;i<b;i++){
        result=result*a;
    }
    return result;
}
int len(int a){
    int b,count;
    while(a!=0){
        b=a%10;
        a=a/10;
        count++;
    }
    return count;
}
void armstrong( int a , int n){
    int original=a,i,b,c=0;
    for(i=0;i<n;i++){
        b=a%10;
        c=c+power(b,n);
        a=a/10;
    }
    if(c==original){
        printf("yes");
    }
    else{
        printf("no");
    }
}
int main(){
    int a,n;
    printf("enter no ");
    scanf("%d",&a);
    n=len(a);
    armstrong(a,n);
}