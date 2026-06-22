//write a function for sum of digit.
#include<stdio.h>
void FunSumDigit(){
	int num,sum=0,digit;
	printf("Enter Number:");
	scanf("%d",&num);
	while(num!=0){
		digit=num%10;
		sum+=digit;
		num=num/10;
	}
	printf("Sum of Digit is %d.",sum);
}
main(){
	FunSumDigit();
	return 0;
}
