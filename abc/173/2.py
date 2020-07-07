N = int(input())
A = list(input() for _ in range(N))

print("AC x",A.count("AC"))
print("WA x",A.count("WA"))
print("TLE x",A.count("TLE"))
print("RE x",A.count("RE"))