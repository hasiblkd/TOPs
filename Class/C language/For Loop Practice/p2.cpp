#include<stdio.h>
main(){
	
	int num,i;
	
	printf("Enter Number::");
	scanf("%d", &num);
	
	for(i=1;i<=num;i=i+2){
		printf("%d\n", i);
	}
	
}
