def factor(N):
    f = []
    for i in range(1,int(N**0.5)+1):
        if N%i == 0:
            f.append(i)
    return sorted(list(set(f)))

def f(A,B):
    return max(len(str(A)),len(str(B)))

N = int(input())
m = 1e9
for n in factor(N):
    m = min(f(n,N//n),m)

print(m)

