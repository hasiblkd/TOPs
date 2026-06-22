//Count string Lenght
#include<stdio.h>
main(){
	char str[10];
	int i=0,count=0;
	printf("\n Enter String:");
	scanf("%s",&str);
	while(str[i]!='\0'){
		count++;
		i++;
	}
	printf("Lenght of String is %d.",count);
} 
