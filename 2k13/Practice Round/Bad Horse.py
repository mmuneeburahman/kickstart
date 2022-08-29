T = int(input())
for i in range(T):
    M = int(input())
    probs = {}
    for j in range(M):
        pair = input()
        pair = pair.split(' ')
        if pair[0] in probs:
            probs[pair[0]].append(pair[1])
        else:
            probs[pair[0]] = [pair[1]]
        if pair[1] in probs:
            probs[pair[1]].append(pair[0])
        else:
            probs[pair[1]] = [pair[0]]
    # visited = {}
    colors = {}
    for key in probs.keys():
        # visited[key] = False
        colors[key] = -1
    cont = True
    for key, value in probs.items():
        if colors[key] == -1:
            colors[key] = 1
            stack = []
            stack.append(key)
            while len(stack) and cont:
                person = stack.pop()
                for neigbor in probs[person]:
                    if colors[neigbor] == colors[person]:
                        print("case==", neigbor, person)
                        cont = False
                    if colors[neigbor] == -1:
                        print(f'color assigned to {neigbor} is {(colors[person]+1)%2}')
                        colors[neigbor] = ((colors[person]+1)%2)
                        stack.append(neigbor)
    a = None
    if cont:
        a = f'Case #{i+1}: Yes'
        print(a)
    else:
        a = f'Case #{i+1}: No'
        print(a)