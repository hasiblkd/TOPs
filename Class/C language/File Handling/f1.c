#include<stdio.h>
main(){
	FILE *fp;
	char data[20];
	fp=fopen("hello.txt","w");
	fprintf(fp,"%s","Hello Hasib...");
	fclose(fp);
	
	fp=fopen("hello.txt","r");
	fgets(data,20,fp);
	printf("\nReading File\n%s",data);
	fclose(fp);
}
