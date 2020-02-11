N = []

for i in range(6):
    N.append(int(input()))

ans = "Yay!"
for i in range(5):
    for j in range(i+1,5):
        dist = abs(N[j] - N[i])
        
        if dist > N[5]:
            ans = ":("

print(ans)

##5m