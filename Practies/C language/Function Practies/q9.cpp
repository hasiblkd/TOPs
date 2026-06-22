//Write a function for find sum and avrage.
#include<stdio.h>
int FunSum(int num1,int num2,int num3){
	return num1+num2+num3;
}
float FunAvg(int sum){
	return sum/3.0;
}
int main(){
	int num1,num2,num3,result1;
	float result2;
	printf("\nEnter Number 1:");
	scanf("%d",&num1);
	printf("\nEnter Number 2:");
	scanf("%d",&num2);
	printf("\nEnter Number 3:");
	scanf("%d",&num3);
	result1=FunSum(num1,num2,num3);
	printf("\nSum of %d + %d + %d is %d.",num1,num2,num3,result1);
	result2=FunAvg(result1);
	printf("\nAvrage is %f.",result2);
}
