//Full pyramid
#include<stdio.h>
main(){
	
	int num,i,j,k;
	
	printf("Enter Number::");
	scanf("%d", &num);
	
	for(i=1;i<=num;i++){
		for(k=num;k>=i-1;k--){
			printf(" ");
		}
		for(j=1;j<=i;j++){
				printf("* ");
			}
		printf("\n");
	}
	
}
