#include <bits/stdc++.h>
using namespace std;
using ll = long long;
const ll M = 1e9+7;

ll modpow(ll base, ll pow, ll mod){
    if (pow==0) return 1%mod;
    if (pow==1)return base%mod;

    ll res = modpow(base*base%mod, pow/2, mod);
    if (pow%2==1) return (base*res)%mod;
    return res;
}
ll solve(){
    ll a, b, n, k;
    cin>>a>>b>>n>>k;
    vector<ll> cnts(k);
    for(int i =1; i<=min(n, k);i++){
        ll num = ((n-i)/k+1)%M;
        ll modp = modpow(i, b, k);
        cnts[modp] = (cnts[modp]+num)%M;
    }
    ll res = 0;
    for(int i =1; i<=min(n, k); i++) {
        ll num = ((n-i)/k+1)%M;
        ll targmod = (k-modpow(i, a, k))%k;
        res+=(cnts[targmod]*num)%M;
        if (modpow(i, b, k)==targmod)
            res+=M-num;
    }
    return res%M;
}
int main(){
    int T;
    cin>>T;
    for(int i = 1; i<=T; ++i){
        cout<<"Case #"<<i<<": "<<solve();
    }
}