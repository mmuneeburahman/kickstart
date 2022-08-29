T = int(input())
for t in range(T):
    N = int(input())
    vs = input()
    vs = vs.split(' ')
    vs = list(map(int, vs))
    ol = []
    el = []
    for v in vs:
        if v%2==0:
            el.append(v)
        else:
            ol.append(v)
    ol = sorted(ol)
    el = sorted(el)
    odd_index = 0
    for i, v in enumerate(vs):
        if v%2!=0:
            vs[i] = ol[odd_index]
            odd_index+=1
    even_index = len(el)-1
    for i, v in enumerate(vs):
        if int(v)%2==0:
            vs[i] = el[even_index]
            even_index-=1
    print(f'Case #{t+1}:', *vs)