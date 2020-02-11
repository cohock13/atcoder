#include<bits/stdc++.h>
#define rep(i, n) for(int i=0; i<(n); i++)

using namespace std;

int main(void){
    int N,M;

    cin>>N;cin>>M;

    vector<long long> A(N);
    rep(i,N){cin>>A[i];}

    sort(A.begin(),A.end());
    
    while(M>0){
        A[N-1] /= 2;
        sort(A.begin(),A.end());
        M -= 1;
    }
    long long ans = 0;
    rep(i,N){
        ans += int(A[i]);
    }

    cout<<ans;
    return 0;
    


}


