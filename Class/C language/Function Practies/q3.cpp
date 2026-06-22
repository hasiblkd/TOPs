//Write a function to check prime number.
#include<stdio.h>
int FunPrime(){
	int num,i,flag=0;
	printf("\nEnter Number to Check Prime Number:");
	scanf("%d",&num);
	for(i=2;i<=num/2;i++){
		flag=1;
		break;
	}
	if(flag==0){
			printf("\n%d is Prime Number.",num);
		}else{
			printf("\n%d is not Prime Number.",num);
	}
}
main(){
	FunPrime();
	return 0;
}
