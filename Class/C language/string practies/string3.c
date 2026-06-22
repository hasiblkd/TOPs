//Reverse String
#include<stdio.h>
main(){
	char str[10],rev[10];
	int i=0,j,k=0,count=0;
	printf("Enter String:");
	scanf("%s",&str);
	//find lenght
	while(str[i]!='\0'){
		count++;
		i++;
	}
	//reversing index
	i--;
	j=i;
	while(j>=0){
		//store value in rev veriable
		rev[k]=str[j];
		k++;
		j--;
	}
	printf("Reverse String is %s.",rev);
	
}
