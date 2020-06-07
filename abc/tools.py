##階乗
import math
def fact(n):
    return math.factorial(n)
##10 -> n 進法変換,逆はint(num,base)
def base_10_to_n(X, n):
    if (int(X/n)):
        return base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

##繰り返し二乗法 O(log
# n)
##pow(n,m,mod)であるのでこっちを使おう
def pow(x, n):
      ans = 1
  while(n > 0):
    if(bin(n & 1) == bin(1)):
      ans = ans*x
    x = x*x
    n = n >> 1 #ビットシフト
  return ans

##組み合わせ By階乗 nが小さいとき向け
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
##組み合わせ(コンビネーション) By DP O(N)
nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]
##組み合わせ modで割ったあまりを出力する場合 O(r)
def combination(n,r,mod=10**9+7):
    n1 = n+1
    r = min(r,n-r)
    numer = denom = 1
    for i in range(1,r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom,mod-2,mod) % mod

##mod table
"""
https://www.planeta.tokyo/entry/5195/
"""
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10**9+7
n = 10**5+1  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
 
for i in range(2, n + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)


#gcd,lcm 
#Atcoderではmath.gcdは使えないので注意!!
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a, b):
    return (a * b)//gcd(a,b)

from fractions import gcd##でもいける。
##Python3.8になればfrom math import gcd が通る

##素数判定
import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

#素因数分解(返り値はlist)
def prime_factorize(N): #素因数分解
    exponent = 0
    while N%2 == 0:
        exponent += 1
        N //= 2
    if exponent: factorization = [[2,exponent]]
    else: factorization = []
    i=1
    while i*i <=N:
        i += 2
        if N%i: continue
        exponent = 0
        while N%i == 0:
            exponent += 1
            N //= i
        factorization.append([i,exponent])
    if N!= 1: factorization.append([N,1])
    assert N != 0, "zero"
    return factorization

##順列生成
import itertools
for x in itertools.permutations(a):

import bisect
import heapq
import itertools
import math
import operator
import os
import re
import string
import sys
from collections import Counter, deque, defaultdict
from copy import deepcopy
from decimal import Decimal
from fractions import gcd
from functools import lru_cache, reduce
from operator import itemgetter, mul, add, xor

import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
def input(): return sys.stdin.readline().strip()
def STR(): return input()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
sys.setrecursionlimit(10 ** 9)
inf = sys.maxsize
mod = 10 ** 9 + 7