//Palindrome Number using function
#include<stdio.h>
int FunPalindromeNum(){
	int temp,num,rev=0,digit;

	printf("Enter Number:");
	scanf("%d",&num);
	
	temp=num;
	
	while(num!=0){
		digit=num%10;
		num=num/10;
		rev=rev*10+digit;
	}
	if(rev==temp){
		printf("%d is Palindrome Number.",temp);
	}else{
		printf("%d is not Palindrome Number.",temp);
	}
	
}
main(){
	FunPalindromeNum();
	return 0;
}
