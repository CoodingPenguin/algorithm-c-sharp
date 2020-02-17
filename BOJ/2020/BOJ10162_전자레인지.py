def min_btn(t):
    if t % 10 != 0:
        print(-1)
        return

    btns = [300, 60, 10]
    time = [0] * 3

    for i in range(3):
        while t - btns[i] >= 0:
            time[i] += 1
            t = t - btns[i]

    print(time[0], time[1], time[2])


T = int(input())
min_btn(T)
