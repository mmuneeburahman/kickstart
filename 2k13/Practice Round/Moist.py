T = int(input())
for i in range(T):
    N = int(input())
    last = input()
    count = 0
    for j in range(N-1):
        now = input()
        if now<last:
            count+=1
        else:
            last = now
    print(f'Case #{i+1}: {count}')