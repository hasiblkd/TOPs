#include<stdio.h>
int funSqure(){
	int s,num;
	printf("\nEnter Number:");
	scanf("%d",&num);
	s=num*num;
	printf("\nArea of Squre is %d.",s);
}
int funRectangle(){
	int l,w,ans;
	printf("\nEnter Area of Lenght:");
	scanf("%d",&l);
	printf("\nEnter Area of Weight:");
	scanf("%d",&w);
	ans=l*w;
	printf("\nArea of Rectangle is %d.",ans);

}
float funTringle(){
	int b,h;
	float area;
	printf("\nEnter Base of Triangle:");
	scanf("%d",&b);
	printf("\nEnter Height of Triangle:");
	scanf("%d",&h);
	area=(b*h)/2;
	printf("\nArea of Triangle is %f.",area);
}
float funCricle(){
	int r;
	float area;
	printf("\nEnter the Redius of Cricle:");
	scanf("%d",&r);
	area=3.14*r*r;
	printf("\nArea of Cricle is %f.",area);
	
}
int main(){
	int ch,i;
	for(;;){
		printf("\n===== AREA CALCULATOR MENU =====\n");
		printf("1. Area of Square\n");
		printf("2. Area of Rectangle\n");
		printf("3. Area of Triangle\n");
		printf("4. Area of Circle\n");
		printf("5. Exit\n");
		printf("Enter your choice: ");
		scanf("%d",&ch);
		switch(ch){
		case 1:
			funSqure();
			break;
		case 2:
			funRectangle();
			break;
		case 3:
			funTringle();
			break;
		case 4:
			funCricle();
			break;
		case 5:
			printf("Exitting program......\n");
			return 0;
		default:
			printf("Invalied Choice.......");
			break;
	}
	}
}
