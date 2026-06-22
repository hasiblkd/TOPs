#include<stdio.h>
//function without returntype without parameter
void Funmsg(){
	printf("\nHello World!");
}
//function without returntype with parameter
void FunAdd(int a,int b){
	int c;
	c=a+b;
	printf("\nAddition is %d",c);
}
//function with returntype with parameter
int funSqure(int num){
	int s;
	s=num*num;
	return s;
}
//function with returntype without parameter
float areaOfCricle(){
	int r;
	float area;
	printf("\nEnter number:");
	scanf("%d",r);
	area=3.14*r*r;
	return area;
}
main(){
	Funmsg();
	FunAdd(4,3);
	int s=funSqure(12);
	printf("\nSqure is %d.",s);
	float a=areaOfCricle();
	printf("\narea of cricle is %f.",a);
}
