#include<stdio.h>

void swap(int a , int b){
    int temp;
    temp=a;
    a=b;
    b=temp;
    printf("after swap , first no is %d and 2nd no is %d",a,b);
}
int main(){
    int a,b;
    printf("enter 1st and 2nd no");
    scanf("%d %d",&a,&b);
    
    swap(a,b);

}