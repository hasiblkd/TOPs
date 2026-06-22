//Count Vowel in String
#include<stdio.h>
#include<string.h>
main(){
	char str[99];
	int i,cntVowel=0;
	printf("Enter String:");
	scanf("%s",&str);
	while(str[i]!='\0'){
		if(str[i]=='a' || str[i]=='e' ||str[i]=='i' ||str[i]=='o' || str[i]=='u' || 
		   str[i]=='A' || str[i]=='E' || str[i]=='I' || str[i]=='O' || str[i]=='U'){
			cntVowel++;
		}
		i++;
	}
	if(str[i]==0){
		printf("No Vowel's in Given String........");
	}else{
		printf("Total Vowel's in Given String is %d.",cntVowel);
	}
}
