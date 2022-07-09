import sys

sys.setrecursionlimit(10 ** 9) # RecursionError가 발생하여 한도를 강제로 설정하여 높인다.

input = sys.stdin.readline

# 트리 입력
tree = list()
count = 0
while count <= 10000:
    try:
        node = int(input())
        tree.append(node)

    except:
        break

    count += 1


def solution(start, end):
    # 탐색 종료 조건
    if start > end:
        return

    div = end + 1

    # root ( = tree[start]) 보다 큰 값이 나올때 까지 탐색 시작
    for i in range(start + 1, end + 1):
        if tree[start] < tree[i]:
            div = i
            break

    # 왼쪽 서브 트리
    solution(start + 1, div - 1)
    # 오른쪽 서브 트리
    solution(div, end)

    # 자기 자신 root node
    print(tree[start])


solution(0, len(tree) - 1)
