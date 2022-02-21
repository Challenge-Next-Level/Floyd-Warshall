"""
list_b를 정렬한다.
list_a의 항목 하나 하나 씩, list_b를 이분탐색한다.
"""
t = int(input())

for _ in range(t):
    result = 0

    num_a, num_b = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    list_b.sort()

    for a in list_a:
        start, end = 0, len(list_b) - 1
        res = -1  # list_b의 가장 처음

        while start <= end:
            mid = (start + end) // 2

            # 찾고자 하는 값(a) 이 더 오른쪽에 있음
            if list_b[mid] < a:
                res = mid
                start = mid + 1
            else:
                end = mid - 1

        result += res + 1  # 인덱스를 활용하기 때문

    print(result)
