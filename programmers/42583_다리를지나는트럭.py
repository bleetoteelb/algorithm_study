def solution(bridge_length, weight, truck_weights):
    in_bridge = []
    total_weight = 0
    truck_cnt = len(truck_weights)
    time = 1
    i = 0
    while(True):
        while in_bridge and ((time - in_bridge[-1][0]) == bridge_length):
            total_weight -= in_bridge[-1][1] 
            in_bridge.pop() 
        if (i < truck_cnt) and (total_weight + truck_weights[i] <= weight):
            in_bridge.insert(0,(time,truck_weights[i]))
            total_weight += truck_weights[i]
            i += 1
        if (i == truck_cnt) and not in_bridge:
            break;
        if (i == truck_cnt) or (total_weight + truck_weights[i] > weight):
            time = in_bridge[-1][0] + bridge_length
        else:
            time += 1
    return time
