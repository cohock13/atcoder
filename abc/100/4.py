N,M = map(int,input().split())

ppp = []
mpp = []
pmp = []
ppm = []
pmm = []
mpm = []
mmp = []
mmm = []

for i in range(N):
    x,y,z = map(int,input().split())
    ppp.append(x+y+z)
    mpp.append(-x+y+z)
    pmp.append(x-y+z)
    ppm.append(x+y-z)
    pmm.append(x-y-z)
    mpm.append(-x+y-z)
    mmp.append(-x-y+z)
    mmm.append(-x-y-z)

ans = []
ppp.sort(reverse=True)
ans.append(sum(ppp[:M]))
mpp.sort(reverse=True)
ans.append(sum(mpp[:M]))
pmp.sort(reverse=True)
ans.append(sum(pmp[:M]))
ppm.sort(reverse=True)
ans.append(sum(ppm[:M]))
pmm.sort(reverse=True)
ans.append(sum(pmm[:M]))
mpm.sort(reverse=True)
ans.append(sum(mpm[:M]))
mmp.sort(reverse=True)
ans.append(sum(mmp[:M]))
mmm.sort(reverse=True)
ans.append(sum(mmm[:M]))

print(max(ans))








