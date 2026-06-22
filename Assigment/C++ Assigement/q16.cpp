#include<iostream>
using namespace std;
int main(){
    int a[99][99],b[99][99],ans[99][99];
    int i,j;
    cout<<"============ Matrix 1 ============"<<endl;
    for(i=0;i<2;i++){
        for(j=0;j<2;j++){
            cout<<"Enter Number :";
            cin>>a[i][j];
        }
    }
    cout<<"============ Matrix 2 ============"<<endl;
    for(i=0;i<2;i++){
        for(j=0;j<2;j++){
            cout<<"Enter Number :";
            cin>>b[i][j];
        }
    }
    cout<<"============  Sum of Matrix  ============"<<endl;
    for(i=0;i<2;i++){
        for(j=0;j<2;j++){
            ans[i][j]=a[i][j]+b[i][j];
        }
    }
    for(i=0;i<2;i++){
        for(j=0;j<2;j++){
            cout<<ans[i][j]<<" ";
        }
        cout<<"\n";
    }
}