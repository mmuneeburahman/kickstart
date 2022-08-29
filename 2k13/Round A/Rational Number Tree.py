T = int(input())
for t in range(T):
    query = input().split(" ")
    if query[0] == "1":
        n = int(query[1])-1
        path = []
        while n != 0:
            parent = (n-1)//2
            if 2*parent+1==n:
                path.append("L")
                n=parent
            if 2*parent+2==n:
                path.append("R")
                n=parent
        p = 1
        q = 1
        while path:
            turn = path.pop()
            if turn == "R":
                p+=q
            if turn == "L":
                q+=p
        print(f'Case #{t+1}: {p} {q}')
    if query[0] == "2":
        p = int(query[1])
        q = int(query[2])
        path = []
        while p!=1 or q!=1:
            if p>q:
                p-=q
                path.append("R")
            if q>p:
                q-=p
                path.append("L")
        n = 0
        while path:
            turn = path.pop()
            if turn =="L":
                n=2*n+1
            if turn == "R":
                n=2*n+2
        print(f'Case #{t+1}: {n+1}')