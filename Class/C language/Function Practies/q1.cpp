// write function that print 1 to N numbers.
#include<stdio.h>
void printNum(){
	int i,num;
	printf("Enter number(1-N)::");
	scanf("%d",&num);
	for(i=1;i<=num;i++){
		printf("i=%d\n",i);
	}
}
main(){
	printNum();
}
