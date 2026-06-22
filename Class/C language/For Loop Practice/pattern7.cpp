//Rhombus Pyramid
#include<Stdio.h>
main(){
	int num,i,j,k;
	
	printf("Enter number:");
	scanf("%d",&num);
	
	for(i=1;i<=num;i++){
		for(k=1;k<=i-1;k++){
			printf(" ");
		}
		for(j=1;j<=num;j++){
			printf("* ");
		}
		printf("\n");
	}
	
}
