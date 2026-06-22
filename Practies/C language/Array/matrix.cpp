//2d Matrix
#include<stdio.h>
main(){
	int i,j,a[2][2];
	printf("\n Enter 2D Matrix\n");
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			printf("\nEnter a[%d][%d]",i,j);
			scanf("%d",&a[i][j]);
		}
	}
	//print Matrix
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			printf("\n2D matrix Value is %d",a[i][j]);
		}
	}
}
