#include<iostream>

using namespace std;

int main(void){
    int N;
    int A[15];
    int x[14][2],y[14][2];
    int i,j,k;
    cin>>N;
    for(i=0;i<N;++i){
        cin>>A[i];
        for(j=0;j<A[i];++j){
            cin>>x[i][j];cin>>y[i][j];
        }
    }
}