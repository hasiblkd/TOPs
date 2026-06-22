#include<stdio.h>
main(){
	char str[10],str2[10];
	printf("Enter a String:");
	scanf("%s",&str);
	printf("String is %s",str);
	printf("\nEnter a String2:");
	gets(str2);
	puts(str2);
}
