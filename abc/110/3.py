S = input()
T = input()

def chr_count(S):
    count = [0]*1000
    for i in S:
        count[ord(i)] += 1
    return count

Sc = chr_count(S)
Tc = chr_count(T)
Sc.sort()
Tc.sort()

if Sc == Tc:
    print("Yes")
else:
    print("No")


