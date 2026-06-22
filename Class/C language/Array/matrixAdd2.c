//Addition of Matrix
#include<stdio.h>
int main(){
	int a[99][99],b[99][99],sum[99][99];
	int i,j,row,col;
	printf("\nEnter No. of rows::");
	scanf("%d",&row);
	printf("\nEnter No. of Column::");
	scanf("%d",&col);
	printf("\nEnter Matrix A values.....");
	for(i=0;i<row;i++){
		for(j=0;j<col;j++){
			printf("\nEnter Number::");
			scanf("%d",&a[i][j]);
		}
	}
	printf("\nEnter Matrix b values.....");
	for(i=0;i<row;i++){
		for(j=0;j<col;j++){
			printf("\nEnter Number::");
			scanf("%d",&b[i][j]);
		}
	}
	printf("\nAddition's of Matrix.....");
	for(i=0;i<row;i++){
		for(j=0;j<col;j++){
			sum[i][j]=a[i][j]+b[i][j];
			printf("\nAddition of Matrix is %d.",sum[i][j]);
		}
		printf("\n");
	}
	return 0;
}
