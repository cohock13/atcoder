
S = set(input())

for i in range(97,97+26):
    if chr(i) not in S:
        print(chr(i))
        exit()

print("None")
