from collections import Counter

N = int(input())
S = []
for i in range(N):
    S.append(input())

count = Counter(S).most_common()
mode = count[0][1]
count.sort()
##print("--")
for i in range(len(count)):
    if count[i][1] == mode:
        print(count[i][0])
