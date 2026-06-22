#include<stdio.h>
struct User{
	int uid; 
	char sname[30];
	char email[50];
	int std;
};//reffernce of Structer
int main(){
	struct User u1={101,"Hasib","hasiblakdawala@gmail.com",12};
	printf("\nUid is %d.",u1.uid);
	printf("\nSname is %s.",u1.sname);
	printf("\nEmail is %s.",u1.email);
	printf("\nStd is %d.",u1.std);
}
