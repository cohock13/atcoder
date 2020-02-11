N = int(input())
S = input()
ans = 0

for i in range(len(S)-2):
    tmp = 0
    if S[i]=="A" and S[i+1] == "B" and S[i+2] == "C":
        ans += 1

print(ans)