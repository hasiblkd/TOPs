//Count digits of a number using function.
#include<stdio.h>
void FunCountDigit(){
	int num,count=0,reminder;
	printf("Enter Number:");
	scanf("%d",&num);
	if(num==0){
		count=1;
	}else{
		while(num!=0){
		num=num/10;
		count++;
	}
	}
	printf("Total Digit is %d.",count);
	//return count;
}
main(){
	FunCountDigit();
	return 0;
}
