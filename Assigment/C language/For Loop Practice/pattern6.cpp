//Inverted Full pyramid
#include<stdio.h>
main(){
	
	int num,i,j,k;
	
	printf("Enter Number::");
	scanf("%d", &num);
	
	for(i=1;i<=num;i++){
		for(k=1;k<=i-1;k++){
			printf(" ");
		}
		for(j=1;j<=num-i+1;j++){
				printf("* ");
			}
		printf("\n");
	}
	
}
