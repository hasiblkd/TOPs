#include<stdio.h>
int funInput(){
	int num1;
	printf("Enter Number:");
	scanf("%d",&num1);
	return num1;
}
int funTable(int num){
	int i;
	for(i=1;i<=10;i++){
		printf("\n%d * %d = %d\n",num,i,num*i);
	}
}
int main(){
	int result;
	result=funInput();
	int result2;
	result2=funTable(result);
}
