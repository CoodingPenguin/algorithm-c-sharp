
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
def extract_string(s):
    number = ''
    string = ''
    for i, letter in enumerate(s):
        if letter.isalpha():
            string = s[i:]
            break
        number += letter
    return number, string

def solution(s):
    length = len(s)
    result = length
    for i in range(1, length//2+1):
        stack = [s[0:i]]
        for j in range(i, length, i):
            target = s[j:j+i]
            top = stack[-1]
            number, string = extract_string(top)
            if target == string:
                stack.pop()
                if number == '':
                    stack.append('2'+string)
                else:
                    stack.append(str(int(number)+1)+string)
            else:
                stack.append(target)
        stackLength = len(''.join(stack))
        if stackLength < result:
            result = stackLength
    return result