from functools import reduce

mult = lambda x,y:x*y

def factorial(n):
  if n in (0, 1):
    return 1
  return reduce(mult, range(1, n+1))

n, k = map(int, input().split())
result = factorial(n)//factorial(k)//factorial(n-k)

print(result%10007)
