//find Largest number
#include<stdio.h>
void LargeFun(){
	int num1,num2,num3;
	
	printf("\nEnter Number 1:");
	scanf("%d",&num1);
	printf("\nEnter Number 2:");
	scanf("%d",&num2);
	printf("\nEnter Number 3:");
	scanf("%d",&num3);
	
	if(num1>=num2 && num1>=num3){
		printf("%d is Largest Number.",num1);
	}else if(num2>=num1 && num2>=num3){
		printf("%d is Largest Number.",num2);
	}else if(num3>=num1 && num3>=num2){
		printf("%d is Largest Number.",num3);
	}
}
main(){
	LargeFun();
	return 0;
}
