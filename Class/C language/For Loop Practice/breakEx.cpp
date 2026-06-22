#include<Stdio.h>
main(){
	int i,num;
	
	for(i=1;i<=10;i++){
		if(i==10 || i==7){
			continue;
		}
		printf("\n i=%d",i);
	}
	for(;;){
		printf("\n Enter Num:");
		scanf("%d",&num);
		if(i==0){
			break;
		}
	}
}
