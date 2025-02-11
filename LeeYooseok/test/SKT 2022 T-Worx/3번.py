def solution(n, plans, clients):
    answer = []

    # key = 데이터, values = 제공 부가 서비스
    plan_dict = dict()
    service = list()
    for p in plans:
        plan = list(map(int, p.split()))
        plan_service = [0] * (n+1)
        service.extend(plan[1:])
        for s in service:
            plan_service[s] = 1
        plan_dict[plan[0]] = plan_service

    # 각 고객별로 확인
    for i in range(len(clients)):
        client = list(map(int, clients[i].split()))

        # 고객 최소 데이터
        client_data = client[0]
        # 고객이 이용하려는 부가 서비스
        client_service = client[1:]

        plan_flag = False # 만족하는 요금제가 있으면 True
        # 각 요금제별로 확인
        for num in range(len(plan_dict.keys())):
            plan_data = list(plan_dict.keys())[num]
            # 요금제 데이터 >= 고객이 원하는 최소 데이터
            if plan_data >= client_data:
                service_flag = True # 고객이 원하는 부가 서비스가 없다면 False
                for s in client_service:
                    if plan_dict[plan_data][s] == 0:
                        service_flag = False
                        break
                if service_flag: # 고객이 원하는 모든 부가 서비스가 있다면
                    answer.append(num + 1)
                    plan_flag = True
                    break
        # 고객에게 만족하는 요금제가 없다면 0
        if not plan_flag:
            answer.append(0)

    return answer

print(solution(5, ["100 1 3", "500 4", "2000 5"], ["300 3 5", "1500 1", "100 1 3", "50 1 2"]))