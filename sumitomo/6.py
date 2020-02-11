T1,T2 = map(int,input().split())
A1,A2 = map(int,input().split())
B1,B2 = map(int,input().split())

dis1 = (A1 - B1) * T1
dis2 = (A2 - B2) * T2
"""
if dis1 + dis2 <0:
    print(0)

elif dis1 == -dis2:
    print("infinity")
"""

if dis1 + dis2 == 0:
    print("infinity")

elif (dis1+dis2<0 and ):
    print(0)

else:
    S = dis1//(dis1+dis2)
    R = dis1%(dis1+dis2) 
    if R == 0:
        ans = S*2 
    else:
        ans = S*2 + 1
    
    print(abs(ans))
 