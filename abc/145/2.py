N = int(input())
S = input()
if len(S)%2 == 1:
  print("No")
elif S[:int(len(S)/2)]==S[int(len(S)/2):]:
  print("Yes")
else:
  print("No")