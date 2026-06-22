#include<stdio.h>
main(){
	
	int num,i;
	
	printf("Enter Any Number::");
	scanf("%d", &num);
	
	for(i=5;i>=num;i--){
		printf("%d\n", i);
	}
	
}
