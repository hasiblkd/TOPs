//inverted Left half pyramid
#include<stdio.h>
main(){
	
	int num,i,j;
	
	printf("Enter Number::");
	scanf("%d", &num);
	
	printf("Inverted left half pyramid.\n");
	printf("\n");
	for(i=1;i<=num;i++){
		//space loop
		for(j=1;j<=i-1;j++){
			printf(" ");
		}
		//star loop
		for(j=1;j<=num-i+1;j++){
			printf("*");
		}
		printf("\n");
	}
	
}
