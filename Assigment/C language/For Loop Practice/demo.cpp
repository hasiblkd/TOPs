#include<stdio.h>
main(){
	int i,j,num,num2;
	printf("Enter a number:");
	scanf("%d",&num);
	printf("Enter a number:");
	scanf("%d",&num2);
	for(i=1;i<=10;i++){
		printf("%d * %d = %d\t%d * %d = %d\n",num,i,num*i,num2,i,num2*i);
	}
	return 0;
}
