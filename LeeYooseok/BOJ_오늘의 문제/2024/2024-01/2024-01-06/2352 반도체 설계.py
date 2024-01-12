# LST (Longest Increasing Subsequence) 가장 긴 증가하는 부분수열
# 출발지점을 오름차순으로 넣을때, 종료지점이 증가하는 수열이면 -> 꼬이지 않게된다.

n = input()
dest = list(map(int, input().split()))


# 삽입할 위치를 이분 탐색으로 찾음
# arr 에서 val 보다 작으면서 가장 큰값 다음의 인덱스를 반환 = arr을 정렬된 상태로 유지하면서 val이 삽입될 수 있는 위치들 중 가장 인덱스가 작은 것
# lower bound 를 찾는 과정
def binary_search_left(arr, val):
    s, e = 0, len(arr) - 1
    while s <= e:
        m = (s + e) // 2
        if arr[m] > val:
            e = m - 1
        else:
            s = m + 1
    return s


link = []
for d in dest:
    # d 선을 추가해도, 선이 꼬이지 않았다면
    # link 의 마지막 도착지점 < 현재 추가하려는 선의 도착지점
    if not link or link[-1] < d:
        link.append(d)
    else:
        # link 를 정렬된 상태로 유지하면서, d 를 삽입할 수 있는 위치들 중 가장 인덱스가 작은 값과 교환
        # link[-1] >= d 인 경우 이기 때문에 바꾸면서 안꼬이고 더 많은 선 을 넣을 수 있는 상태
        link[binary_search_left(link, d)] = d

print(len(link))
