#include<stdio.h>
void printMSG();
void add(int x,int y);
main(){
	printMSG();
	add(20,40);
	add(200,400);
}
void printMSG(){
	printf("\n Hello World.");
}
void add(int x,int y){
	printf("\n Addition of %d and %d = %d",x,y,x+y);
}
