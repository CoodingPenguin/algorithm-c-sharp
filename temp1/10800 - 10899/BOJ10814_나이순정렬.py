import sys

people = []
for _ in range(int(sys.stdin.readline())):
  age, name = sys.stdin.readline().strip().split()
  age = int(age)
  people.append((age, name))

people = sorted(people, key=lambda x:x[0])
for age, name in people:
  print(age, name)