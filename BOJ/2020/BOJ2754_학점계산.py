def result(grade):
    rt = 0
    if grade[0] == "A":
        rt = 4.0
    elif grade[0] == "B":
        rt = 3.0
    elif grade[0] == "C":
        rt = 2.0
    elif grade[0] == "D":
        rt = 1.0
    elif grade[0] == "F":
        rt = 0.0
        return "{:.1f}".format(rt)

    if grade[1] == "+":
        rt += 0.3
    elif grade[1] == "-":
        rt -= 0.3

    return "{:.1f}".format(rt)


print(result(input()))
