//Array of Structer
#include<stdio.h>
struct Fruits{
	int fno;
	char fname[20];
	float price;
};
main(){
	struct Fruits f[5];
	int i;
	for(i=0;i<5;i++){
		printf("Enter Fruits no name price:");
		scanf("%d %s %f",&f[i].fno,f[i].fname,&f[i].price);
	}
	printf("\n Fruits no.  Fruits name Fruits Price");
	for(i=0;i<5;i++){
		printf("\n %d %s %f",f[i].fno,f[i].fname,f[i].price);
	}
}
