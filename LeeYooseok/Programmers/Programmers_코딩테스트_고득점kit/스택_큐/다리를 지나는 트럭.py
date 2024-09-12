def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_trucks = list()
    bridge_weight = 0

    while truck_weights or bridge_trucks:
        # 트럭 나가는지 확인
        if bridge_trucks and (answer - bridge_trucks[0][1]) == bridge_length:
            out_truck = bridge_trucks.pop(0)
            bridge_weight -= out_truck[0]

        # 다리에는 최대 bridge_length 대 만큼의 트럭이 올라갈 수 있고, weight 만큼의 무게를 견딜 수 있음
        if truck_weights and len(bridge_trucks) < bridge_length and bridge_weight < weight:
            truck = truck_weights[0]
            if truck + bridge_weight <= weight:
                bridge_trucks.append([truck, answer])
                bridge_weight += truck
                truck_weights.pop(0)

        answer += 1

    return answer