S = input()
count = 0
for i in range(len(S)):
    if (i+1)%2 == 0:
        if S[i]=="L" or S[i]=="U" or S[i]=="D":
            count+=1
    else:
        if S[i]=="R" or S[i]=="U" or S[i]=="D":
            count+=1

if count==len(S):
    print("Yes")
else:
    print("No")

