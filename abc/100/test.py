import fractions
import functools
from copy import deepcopy
def main():
    n = int(input())
    a = [int(t)for t in input().split()]
 
    a_gcd = functools.reduce(fractions.gcd,a)
    a = [x//a_gcd for x in a]
    gcdlist = []
 
    maxa = 1
    for i in range(n):
        t = deepcopy(a)
        del t[i]
        t_gcd = functools.reduce(fractions.gcd,t)
        maxa = t_gcd if t_gcd>maxa else maxa
 
    print(a_gcd*max(gcdlist))
    
if __name__ == "__main__":
    main()