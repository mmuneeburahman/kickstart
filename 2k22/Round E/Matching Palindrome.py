def is_palindrom(test, left):
    right = len(test)-1-left
    while left<=right and test[left] == test[right]:
        left+=1
        right-=1

    return left>right, left

T = int(input())
for t in range(T):
    N = int(input())
    P = input()
    Q = ""
    left = 0
    for a in P:
        Q+=a
        result, left = is_palindrom(P+Q, left)
        if result:
            break
    print(f'Case #{t+1}: {Q}')
