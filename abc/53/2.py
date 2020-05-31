s = input()
t = s[::-1]

print(len(s)-s.find("A")-t.find("Z"))