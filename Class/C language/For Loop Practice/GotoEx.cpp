#include<stdio.h>
main(){
	int num;
	
	printf("Enter Number:");
	scanf("%d",&num);
	
	if (num%2==0){
		goto Even;
	}else{
		goto Odd;
	}
	Even:{
		printf("\n num is Even.");
		return 0;
	}
	Odd:{
		printf("\n num is Odd.");
		return 0;
	}
}
