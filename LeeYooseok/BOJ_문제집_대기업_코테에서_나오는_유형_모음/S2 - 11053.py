N = int(input())
data = list(map(int, input().split()))


# ans 리스트에서 target 보다 크거나 같은 값들 중 index가 가장 작은 값을 찾는다.
def binary_search(target):
    left, right = 0, len(answer) - 1
    while left <= right:
        mid = (left + right) // 2

        if answer[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


answer = [data[0]]

for i in range(N):
    # 현재 값이 정답 리스트의 모든 값보다 크다면,
    if data[i] > answer[-1]:
        # 정답 리스트 마지막에 추가
        answer.append(data[i])
    # 정답 리스트에 현재 값 보다 큰 값이 있다면
    else:
        # 현재 값이 들어갈 수 있는 위치(현재 값보다 크면서 가장 작은 값)을 찾는다.
        # idx = bisect.bisect_left(answer, data[i])
        idx = binary_search(data[i])

        # 값을 교환한다.
        answer[idx] = data[i]

# LIS의 길이는 구할 수 있지만, LIS자체를 구하지는 못한다...(?)
print(len(answer))