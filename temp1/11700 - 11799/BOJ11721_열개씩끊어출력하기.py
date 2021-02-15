w = input()
l = len(w)
for i in range(0, l//10):
    print(w[i*10:(i+1)*10])
print(w[(l//10)*10:])
