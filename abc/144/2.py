N = int(input())

ans = "No"
for i in range(1,10):
    if (N/i)%1 == 0 and (N/i)<10:
        ans = "Yes"
        break

print(ans)