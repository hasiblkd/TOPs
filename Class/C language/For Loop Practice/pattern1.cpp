#include<stdio.h>
main(){
	int num,i;
	
	printf("Enter Number::");
	scanf("%d", &num);
	for(i=1;i<=num;i++){
		for(int j=1;j<=num;j++){
			printf("* ");
		}
		printf("\n");
	}
	
}
