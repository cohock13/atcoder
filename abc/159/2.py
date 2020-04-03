def pale(string):
    return 1 if string==string[::-1] else 0

S = (input())
N = len(S)
tmp1 = S[:(N-1)//2]
##print(tmp1)
tmp2 = S[(N+3)//2-1:]
##print(tmp2)
if pale(S) and pale(tmp1) and pale(tmp2):
    print("Yes")
else:
    print("No")
