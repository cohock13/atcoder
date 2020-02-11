S = input()

ans = 1e9

for i in range(len(S)-2):
    tmp = 100*int(S[i])+10*int(S[i+1])+int(S[i+2])
    ans = min(ans,abs(753-tmp))

print(ans)