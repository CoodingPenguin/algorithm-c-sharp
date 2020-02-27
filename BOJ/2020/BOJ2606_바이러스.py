N, P = int(input()), int(input())
v = [False]*N; v[0] = True
con = []
for _ in range(P):
    i = sorted(list(map(lambda x:int(x)-1, input().split())))
    con.append(i)
con = sorted(con)
for c in con:
    if v[c[0]] == True and v[c[1]] == False:
        v[c[1]] = True
    elif v[c[0]] == False and v[c[1]] == True:
        v[c[0]] = True

print(v.count(True)-1)
