from collections import defaultdict
 
s = input()
k = int(input())
 
l = len(s)

if k > l:
    print(0)
else:
    patterns = defaultdict()

    for i in range(l-k+1):
        tmp = s[i:i+k]
        patterns[tmp] = 1
    
    print(len(patterns))