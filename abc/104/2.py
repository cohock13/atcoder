S = input()
ans = "WA"
if S[0] == "A":
    tmp = S[2:len(S)-1]
    if tmp.count("C") == 1:
        c = tmp.index("C")
        count = 0
        for i in range(1,len(S)):
            tmp2 = S[i]
            if tmp2.islower():
                count += 1
        if count == len(S) - 2:
            ans = "AC"
print(ans)



    


