# position이라는 리스트 사용이 핵심, 역시 정말 좋은 아이디어, 그러나 충분히 생각해낼 수 있는,,
n = int(input())
crane = list(map(int, input().split()))
crane.sort(reverse=True)
m = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)

moved = [False for _ in range(m)] # 박스를 옮겼는지 체크

if box[0] > crane[0]: # 가장 좋은 크레인이 가장 무거운 박스를 옮기지 못한다면
    print(-1)
else:
    count, time = 0, 0
    position = [0 for _ in range(n)] # 크레인이 다음 search때 어떤 박스부터 찾으면 되는지 index를 저장하는 곳
    while count < m: # 박스 다 옮길 때 까지
        time += 1
        for i in range(n):
            if count >= m: # 박스 다 옮겼으면 break
                break
            idx = position[i]
            for j in range(idx, m): # 옮길 수 있는 박스를 search
                if moved[j] or crane[i] < box[j]: # 이미 옮겼거나 들 수 없는 박스라면 다음 박스를 search
                    position[i] += 1
                    continue
                # 박스를 옮길 수 있다면
                position[i] += 1
                moved[j] = True
                count += 1
                break

    print(time)