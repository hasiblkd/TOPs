#include<stdio.h>
int funArmstrongNum(int num){
	int temp,sum=0,count=0;
	int i,digit,power;
	
	temp=num;
	
	while(temp!=0){
		temp=temp/10;
		count++;
	}
	temp=num;
	while(temp!=0){
		digit=temp%10;
		power=1;
		for(i=1;i<=count;i++){
			power*=digit;
		}
		sum+=power;
		temp/=10;
	}
	if(sum==num){
		return 1;
	}else{
		return 0;
	}
}
int main(){
	int num,result;
	printf("Enter Number:");
	scanf("%d",&num);
	result=funArmstrongNum(num);
	if(result==1){
		printf("%d is Armstrong Number.",num);
	}else{
		printf("%d is not Armstrong Number.",num);
	}
	
}
