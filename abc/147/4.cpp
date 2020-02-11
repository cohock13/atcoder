#include<iostream>

using namespace std;

int main(void){
    unsigned long long N;
    cin>>N;
    unsigned long long A[N],B[N][N]={};
    unsigned long long i,j,ans=0;
    unsigned long long bin = 1e9+7;
    for(i=0;i<N;++i){
        cin>>A[i];
    }
    for(i=0;i<N;++i){
        for(j=i+1;j<N;++j){
            B[i][j] = A[i]^A[j];
        }
    }
    for(i=0;i<N;++i){
        for(j=i+1;j<N;++j){
            ans += B[i][j];
        }
    }

    cout<<ans%bin;
}