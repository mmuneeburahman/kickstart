rules = {
    2: "double",
    3: "triple",
    4: "quadruple",
    5: "quintuple",
    6: "sextuple",
    7: "septuple",
    8: "octuple",
    9: "nonuple",
    10: "decuple"
}
numbers= {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
T = int(input())
for t in range(T):
    line = input()
    line = line.split(' ')
    number = line[0]
    format = line[1]
    i =0
    vs = list(map(int, format.split('-')))
    # print(vs)
    ans = []
    up_to =0
    n = None
    for v in vs:
        count =1
        pre = number[up_to]
        i=1
        while i <v+1:
            if i<v:
                n = number[up_to+i]
            if i<v and n==pre:
                count+=1
            else:
                if count==1:
                    ans.append(numbers[int(pre)])
                elif count<=10:
                    ans.append(rules[count])
                    ans.append(numbers[int(pre)])
                    count = 1
                else:
                    for _ in range(count):
                        ans.append(numbers[int(pre)])
            pre = n
            i+=1
        up_to+=v
    print(f'Case #{t+1}:', *ans)