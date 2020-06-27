S = input()
T = input()

print(sum([int(i!=j) for i,j in zip(S,T)]))