#include<iostream>
using namespace std;

int main(void){
    int N,M;
    cin>>N>>M;
    int ans1 = N*(N-1)/2;
    int ans2 = M*(M-1)/2;
    cout<<ans1+ans2<<endl;
    return 0;
}