def is_right(x, y, z):
      if z**2 == (x**2+y**2):
    return 'right'
  return 'wrong'


while True:
  x, y, z = sorted(map(int, input().split()))
  if not x+y+z:
    break
  print(is_right(x, y, z))
