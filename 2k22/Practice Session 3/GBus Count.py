T = int(input())
for t in range(T):
    N = int(input())
    ranges = list(map(int, input().split()))
    LIMIT = max(ranges)+3
    Xi = [0]*LIMIT
    Yi = [0]*LIMIT
    count = [0]*LIMIT
    for i in range(0, 2*N, 2):
        Xi[ranges[i]]+=1
        Yi[ranges[i+1]+1]+=1

    total =0
    for i in range(LIMIT):
        total=total+Xi[i]-Yi[i]
        count[i] =total
    C = int(input())
    ans = f"Case #{t+1}:"
    for i in range(C):
        P = int(input())
        if P<LIMIT:
            ans=ans+" "+str(count[P])
        else:
            ans=ans+" "+"0"
    print(ans)
    if t+1<T:
        input()