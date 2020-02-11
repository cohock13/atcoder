#include<iostream>
#include<string>

using namespace std;

int main(void){
    int N;
    string S;
    cin>>N;
    cin>>S;
    char a[100001];
    for(int i=0;i<S.length();++i){
       int tmp = S[i] - 'A';
       tmp = (tmp+N)%26;
       putchar('A'+tmp);
    }

    return 0;
}