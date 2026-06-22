//sum of Array Element.
#include<stdio.h>
main(){
	int a[5],sum=0,i;
	printf("Integer Array\n");
	for(i=0;i<5;i++){
		printf("Enter Array Element's a[%d]::\n",i);
		scanf("%d",a[i]);
		sum+=a[i];
	}
	for(i=0;i<5;i++){
		printf("\n a[%d]=%d",i,a[i]);
	}
	printf("\n Addition of Array Element is %d",sum);
}
