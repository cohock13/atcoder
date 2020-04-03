s = input()
K = int(input())
N = len(s)
substring = []

for i in range(min(N,K)):
    for j in range(N-i+1):
        substring.append(s[j:j+i+1])

substring = list(set(substring))
substring.sort()
substring.pop(0)
##print(substring)
print(substring[K-1])

