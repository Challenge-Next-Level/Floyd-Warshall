N = int(input())  # 입력 배열의 크기
arr = list(map(int, input().split()))  # 입력 배열

## 이진탐색 함수
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

lis = [arr[0]]
for i in range(1, len(arr)):
    if arr[i] > lis[-1]:
        lis.append(arr[i])
    else:
        index = binary_search(lis, arr[i])
        lis[index] = arr[i]
print(lis)

