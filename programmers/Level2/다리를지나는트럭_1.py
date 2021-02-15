def solution(bridge_length, weight, truck_weights):
    timer = 0
    bridge = [0] * bridge_length

    while bridge:
        timer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return timer
