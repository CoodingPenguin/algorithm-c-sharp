import sys

def result(stair, n):
    if len(stair) < 3:
        return sum(stair)

    table = [stair[0], max(stair[1], stair[0]+stair[1]), max(stair[0], stair[1])+stair[2]]
    for i in range(3, n):
        table.append(max(stair[i]+stair[i-1]+table[i-3], stair[i]+table[i-2]))
  
    return table[-1]


n = int(sys.stdin.readline())
stair = []
for _ in range(n):
  stair.append(int(sys.stdin.readline()))
print(result(stair, n))
