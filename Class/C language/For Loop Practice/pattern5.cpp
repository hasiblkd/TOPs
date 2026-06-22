//inverted Right half pyramid
#include<stdio.h>
main(){
	
	int num,i,j;
	
	printf("Enter Number::");
	scanf("%d", &num);
	
	printf("inverted Right half pyramid.\n");
	printf("\n");
	for(i=1;i<=num;i++){
		for(j=1;j<=num-i+1;j++){
			printf("*");
		}
		printf("\n");
	}
	
}
