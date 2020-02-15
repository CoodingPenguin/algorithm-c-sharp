def isAlright(test):
    stack = []
    for brkt in test:
        if brkt == "(":
            stack.append(brkt)
        else:
            if len(stack) > 0: stack.pop()
            else: return "NO"    

    if len(stack) == 0: return "YES"
    else: return "NO"
    

TESTCOUNT = int(input())

for n in range(TESTCOUNT):
    print(isAlright(input()))
