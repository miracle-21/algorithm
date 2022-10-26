def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length
    while q:
        q.pop(0)
        time += 1
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return time

    # 정답률 28.6
    # dq = deque(truck_weights)
    # length = 1
    # time = 1
    # item = dq.popleft()
    # while dq:
    #     if item + dq[0] <= weight and length <= bridge_length:
    #         item += dq.popleft()
    #         length += 1
    #         time += 1
    #     else:
    #         item = dq.popleft()
    #         length = 1
    #         time += bridge_length
    # return time + bridge_length