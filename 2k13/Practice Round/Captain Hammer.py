import math
T = int(input())
for i in range(T):
    q = (input())
    vs = q.split(' ')
    V, D = int(vs[0]), int(vs[1])
    value = (D*9.8)/(V**2)
    if value>1:
        value = 1
    elif value<-1:
        value = -1
    ans = math.degrees(math.asin(value))*0.5
    f_ans = "{:.7f}".format(ans)
    print(f'Case #{i+1}: {f_ans}')