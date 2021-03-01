def cal_height(plates):
    height = 10

    for i in range(1, len(plates)):
        if plates[i] == plates[i-1]:
            height += 5
        else:
            height += 10

    return height


plates = input()
print(cal_height(plates))
