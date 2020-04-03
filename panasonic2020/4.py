
from copy import deepcopy
def f(num,N,S):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q"]
    if N == num:
        for i in range(len(S)):
            print(S[i])
        return
    else:
        tmp = []
        length = len(S)
        for i in range(length):
            ttmp = sorted(list(S[i]))
            for j in range(alphabet.index(ttmp[-1])+2):
                tmp.append(S[i]+alphabet[j])
        S = sorted(tmp)
        f(num+1,N,S)
 
N = int(input())
f(1,N,["a"])