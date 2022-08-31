H, W = map(int, input().split())

input_list = list(map(int, input().split()))

ans = 0
# i 위치에 어느정도 물이 담길 수 있는지 확인
for i in range(1, W - 1): # 처음과 끝에는 담길 수 없음
    # i 위치 왼쪽, 오른쪽 가장 높은 벽의 높이를 찾음
    left_max = max(input_list[:i])
    right_max = max(input_list[i+1:])

    # 두개의 벽 중 더 낮은 곳을 기준으로 물이 채워짐
    compare = min(left_max, right_max)

    # 현재 위치가 양쪽 벽들 중 낮은 곳 보다 낮으면 물이 채워짐
    if input_list[i] < compare:
        ans += compare - input_list[i]

print(ans)