#include <stdio.h>
#include <math.h>

int main(){
    int n;
    printf("Please enter the number of consecutive heads required: \n");
    scanf("%d",&n);
    int x=pow(2,n+1)-2;
    printf("The expected number of tosses is %d",x);
    return 0;
}
