from math import ceil, floor
T = int(input())
for t in range(T):
    N = int(input())
    colored = ceil(N/5)
    print(f'Case #{t+1}: {colored}')