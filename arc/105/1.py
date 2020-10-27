A,B,C,D = map(int,input().split())

check1 = (A == (B+C+D) or B ==(A+C+D) or C == (A+B+D) or D == (A+B+C))
check2 = ((A+B) == (C+D) or (A+C) == (B+D) or (A+D) == (B+C))

print("Yes" if check1 or check2 else "No")