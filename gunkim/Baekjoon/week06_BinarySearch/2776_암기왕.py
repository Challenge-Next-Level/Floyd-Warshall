import sys

T = int(sys.stdin.readline().split()[0])


# 우선 시간초과가 처음에 발생했는데 해결법은 아래와 같이 함수로 이분탐색을 하여 return을 해야함.
# 굳이 while문 조건이 만족할때까지 반복을 하지 않고 값을 찾는다면 바로 return 해야함.
def binary_search(n1, num):
    left, right = 0, len(n1) - 1
    while left <= right:
        mid = (left + right) // 2
        if num > n1[mid]:
            left = mid + 1
        else:
            right = mid - 1
        if num == n1[mid]:
            return 1
    return 0


for _ in range(T):
    N = int(input())
    note_1 = list(map(int, sys.stdin.readline().split()))
    M = int(input())
    note_2 = list(map(int, sys.stdin.readline().split()))
    note_1.sort()

    for num in note_2:
        print(binary_search(note_1, num))
