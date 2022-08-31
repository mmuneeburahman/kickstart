from  collections import Counter
right_index = None
def find_mentor(unique_ratings, counts, index):
    global right_index
    mentor = None
    while  index!=right_index and right_index<len(unique_ratings) and unique_ratings[right_index]<=2*unique_ratings[index]:
        mentor = unique_ratings[right_index]
        right_index+=1
    if mentor == None and index-1>=0:
        mentor = unique_ratings[index-1]
    if mentor == None and counts[unique_ratings[index]]>1:
        mentor = unique_ratings[index]
    if mentor == None:
        mentor = -1
    return mentor

T = int(input())
for t in range(T):
    right_index = 1
    N = int(input())
    s_ratings = list(map(int, input().split(' ')))
    counts = Counter(s_ratings)

    unique_ratings = sorted(list(set(s_ratings)))
    mentor_rating = {}
    for i in range(len(unique_ratings)):
        if right_index<=i:
            right_index=i+1
        rating = unique_ratings[i]
        mentor_rating[rating] = find_mentor(unique_ratings,counts, i)
        right_index-=1
       
    ans = [mentor_rating[r] for r in s_ratings]
    print(f'Case #{t+1}:', *ans)

