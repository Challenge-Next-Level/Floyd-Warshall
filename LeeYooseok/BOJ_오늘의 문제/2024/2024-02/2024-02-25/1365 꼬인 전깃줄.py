N = int(input())
line_list = list(map(int, input().split()))

# 가장 긴 증가하는 부분순열

def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    return right


result = [line_list[0]]

for i in range(1, len(line_list)):
    if result[-1] < line_list[i]:
        result.append(line_list[i])
    else:
        # 이분 탐색으로 result 에 line_list[i] 가 들어갈 위치를 찾는다.
        index = binary_search(result, line_list[i])
        result[index] = line_list[i]

print(N - len(result))