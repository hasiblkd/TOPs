#include<stdio.h>
int square(){
	int s,num;
	printf("\nEnter a Square:");
	scanf("%d",&num);
	s=num*num;
	return s;
}
float AreaOfCricle(){
	int r;
	float area;
	printf("\nEnter Redius:");
	scanf("%d",&r);
	area=3.14*r*r;
	return area;
}

main(){
	int ans=square();
	printf("\nSquare is %d",ans);
	float ans2=AreaOfCricle();
	printf("\nArea is %f",ans2);
}
