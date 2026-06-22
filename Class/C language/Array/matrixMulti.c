//Matrix multiplication
#include<stdio.h>
main(){
	int a[99][99],b[99][99],c[99][99];
	int row,col,row2,col2;
	int i,j,k;
	//matrix A
	printf("\nEnter no. of row:");
	scanf("%d",&row);
	printf("\nEnter no. of column:");
	scanf("%d",&col);
	//matrix B
	printf("\nEnter no. of row:");
	scanf("%d",&row2);
	printf("\nEnter no. of column:");
	scanf("%d",&col2);
	if(col!=row2){
		printf("Mutiplication of matrix is not possible....");
		return 0;
	}
	printf("\nEnter Matrix A Values.......");
	for(i=0;i<row;i++){
		for(j=0;j<col;j++){
			printf("\nEnter a number:");
			scanf("%d",&a[i][j]);
		}
	}
	printf("\nEnter Matrix B Values.......");
	for(i=0;i<row2;i++){
		for(j=0;j<col2;j++){
			printf("\nEnter a number:");
			scanf("%d",&b[i][j]);
		}
	}
	//Multiplicatio
	printf("\nMultiplication's of Matrix.......\n");
	for(i=0;i<row;i++){
		for(j=0;j<col2;j++){
			c[i][j]=0;
			for(k=0;k<col;k++){
				c[i][j]+=a[i][k]*b[k][j];
			}
		}
	}
	//printf("Multiplication of Matrix........");
	for(i=0;i<row;i++){
		for(j=0;j<col2;j++){
			printf("%d ",c[i][j]);
		}
		printf("\n");
	}
	return 0;
}
