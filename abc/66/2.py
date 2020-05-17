def check(s):
    if len(s)%2 == 1:
        return False
    if s[len(s)//2:] == s[:len(s)//2]:
        return True
    else:
        return False

S = input()

for i in reversed(range(1,len(S))):
    if check(S[:i]):
        print(i)
        break
