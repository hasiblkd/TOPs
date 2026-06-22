//Write a function to reverse a number (e.g., 123 ? 321).
#include<stdio.h>
void FunRev(){
	int num,i,rev=0,reminder;
	
	printf("Enter Three digit Number:");
	scanf("%d",&num);
	while(num!=0){
		reminder=num%10;
		rev=rev*10+reminder;
		num=num/10;
	}
	printf("Reverse Number is %d.",rev);
	
}
main(){
	FunRev();
	return 0;
}
