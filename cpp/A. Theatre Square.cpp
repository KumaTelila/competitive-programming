#include<bits/stdc++.h>
using namespace std;
int main(){

    double  m, n, a;
    cin>>m>>n>>a;
    long long x = ceil(m/a), y = ceil(n/a);
    
    long long res = x*y;
    cout<<res;
}