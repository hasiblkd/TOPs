#include<stdio.h>
int funInput(){
	int num1;
	printf("Enter Number:");
	scanf("%d",&num1);
	return num1;
}
int funLogic(int num){
	return num*num;
}
int funOutput(int num){
	printf("Answere is %d.",num);
}
int main(){
	int result;
	result=funInput();
	int result2;
	result2=funLogic(result);
	funOutput(result2);
}
