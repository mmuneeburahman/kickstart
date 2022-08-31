def solve(case_num):
    N, M = tuple(map(int, input().split()))
    candies = list(map(int, input().split()))
    total_candies = sum(candies)
    remaining = total_candies%M
    print(f"Case #{case_num}: {remaining}")

T = int(input())
for t in range(T):
    solve(t+1)