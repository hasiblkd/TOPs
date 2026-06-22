//Recursion Function
#include<stdio.h>
int FindFact(int num){
	int f;
	if(num==1){
		return 1;
	}
	f=num*FindFact(num-1);
	return f;
}
main(){
	int f=FindFact(5);
	printf("\n Factorial is %d.",f);
}
