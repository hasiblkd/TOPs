//Addition of Matrix
#include<stdio.h>
int main(){
	int a[2][2],b[2][2],sum;
	int i,j;
	printf("\nEnter Matrix A values.....");
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			printf("\nEnter Number::");
			scanf("%d",&a[i][j]);
		}
	}
	printf("\nEnter Matrix b values.....");
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			printf("\nEnter Number::");
			scanf("%d",&b[i][j]);
		}
	}
	printf("\nAddition's of Matrix.....");
	for(i=0;i<2;i++){
		for(j=0;j<2;j++){
			sum=a[i][j]+b[i][j];
			printf("\nAddition of Matrix is %d.",sum);
		}
	}
}
