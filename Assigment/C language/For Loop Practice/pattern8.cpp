//Dimond Pyramid
#include<stdio.h>
main(){
	int num,i,j,k;
	
	printf("Enter number:");
	scanf("%d",&num);
	//upper body
	for(i=1;i<=num;i++){
		for(k=1;k<=num-i;k++){
			printf(" ");
		}
		for(j=1;j<=i;j++){
			printf("* ");
		}
		printf("\n");
	}
	//lower body
	for(i=num-1;i>=1;i--){
		for(k=1;k<=num-i;k++){
			printf(" ");
		}
		for(j=1;j<=i;j++){
			printf("* ");
		}
		printf("\n");
	}
}
