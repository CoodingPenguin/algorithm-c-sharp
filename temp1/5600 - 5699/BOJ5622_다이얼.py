dial = [3]*3+[4]*3+[5]*3+[6]*3+[7]*3+[8]*4+[9]*3+[10]*4
rt = 0
for n in input():
    rt += dial[ord(n)-ord('A')]
print(rt)
