pados = [0, 1, 1]
for i in range(3, 101):
  pados.append(pados[i-3]+pados[i-2])

for _ in range(int(input())):
  print(pados[int(input())])
