//Write a function that find factorial number.
#include<stdio.h>
int FunFact(){
	int num,i,fact=1;
	printf("Enter Number:");
	scanf("%d",&num);
	for(i=1;i<=num;i++){
		fact*=i;
	}
	printf("Factorial of %d is %d",num,fact);
}
main(){
	FunFact();
	return 0;
}
