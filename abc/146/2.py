N = int(input())
S = input()
L = ""
def f(a):
    return chr((ord(a)+N)%90 + 64) 
for i in range(len(S)):
    if ord(S[i])+N>90:
        s = f(S[i])
    else:
        s = chr(ord(S[i])+N)
    L += s

print(L)