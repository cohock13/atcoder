N = int(input())

h = [2,4,5,7,9]
p = [0,1,6,8]

N = N%10

if N in h:
    print("hon")
elif N in p:
    print("pon")
else:
    print("bon")