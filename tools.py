##階乗
import math
def fact(n):
    return math.factorial(n)

##繰り返し二乗法 O(logn)
##pythonにデフォでpow(x,n,mod)がある
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

##組み合わせ modで割ったあまりを出力する場合 O(r)(1e7位が限界)
def combination(n,r,mod=10**9+7):
    n1 = n+1
    r = min(r,n-r)
    numer = denom = 1
    for i in range(1,r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom,mod-2,mod) % mod

#gcd,lcm 
#Atcoderではmath.gcdは使えないので注意!!
##もう使えます
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

##約数列挙 O(sqrt(N))
def factor(N):
    ans = []
    for i in range(1,int(N**0.5)+1):
        if N%i == 0:
            ans.append(i)
            if N//i != i:
                ans.append(N//i)
    return ans

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

##拡張ユークリッド(https://tech.camph.net/rsa-public-key-encryption/)
def ex_euclid(x, y):
    c0, c1 = x, y
    a0, a1 = 1, 0
    b0, b1 = 0, 1
 
    while c1 != 0:
        m = c0 % c1
        q = c0 // c1
 
        c0, c1 = c1, m
        a0, a1 = a1, (a0 - q * a1)
        b0, b1 = b1, (b0 - q * b1)
 
    return c0, a0, b0

a,b = map(int,input().split())
c,a,b = ex_euclid(a,b)
print(a,b)