
def modpow(base, power, mod):
    if (power == 0): return 1%mod
    if (power == 1): return base%mod
    res = modpow(base*base%mod, power//2, mod)
    if (power%2==1): return (base*res)%mod
    return res

M=1000000007
def solve():
    A, B, N, K = map(int, input().split())
    cnts = [0]*K
    for i in range(1, min(N, K)+1):
        num = ((N-i)//K+1)%M
        modp = modpow(i, B, K)
        cnts[modp] = (cnts[modp]+num)%M
    
    res =0
    for i in range(1, min(N, K)+1):
        num = ((N-i)//K+1)%M
        targmod = (K-modpow(i, A, K))%K
        res+=(cnts[targmod]*num)%M
        
        if modpow(i, B, K) == targmod:
            res+= (M-num)
    return res%M

import time
start_time = time.time()
T = int(input())
for t in range(T):
    print(f"Case #{t+1}: {solve()}")
print("--- %s seconds ---" % (time.time() - start_time))