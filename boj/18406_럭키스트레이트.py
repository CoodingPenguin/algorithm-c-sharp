n = input()
l = len(n)
left = sum(map(int, list(n[:l//2])))
right = sum(map(int, list(n[l//2:])))
if left == right:
  print("LUCKY")
else:
  print("READY")