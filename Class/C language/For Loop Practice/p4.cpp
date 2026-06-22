#include<stdio.h>
main(){
	
	int num,i;
	
	printf("Enter Any Number::");
	scanf("%d", &num);
	
	for(i=10;i>=num;i=i-2){
		printf("Decresed Reverse no is %d\n", i);
	}
	
}
