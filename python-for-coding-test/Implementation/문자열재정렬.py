def result(s):
    alphas, digits = [], []
  
    for letter in s:
        if letter.isalpha():
            alphas.append(letter)
        else:
            digits.append(int(letter))

    alphas.sort()
    result = ''.join(alphas)
    return result + str(sum(digits))

s = input()
print(result(s))