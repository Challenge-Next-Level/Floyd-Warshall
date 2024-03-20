import sys

input = sys.stdin.readline


# 전위, 중위 순회를 입력받아 루트를 찾아 다시 왼쪽, 오른쪽으로 나눈후, 재귀 입력 그 후 루트 출력
def post_order(pre_order, in_order):
    # 서브 트리의 노드 개수가 1 or 2개 일때는 순서대로 출력
    if len(pre_order) == 0:
        return
    elif len(pre_order) == 1:
        print(pre_order[0], end='')
        return
    elif len(pre_order) == 2:
        print(pre_order[1], end='')
        print(pre_order[0], end='')
        return

    # 전위 순회의 가장 앞 자리가 루트 노드이다.
    # root_idx : 중위 순회 결과에서 루트 노드의 위치
    root_idx = in_order.index(pre_order[0])

    # 중위 순회에서 왼쪽 서브트리
    left_in = in_order[:root_idx]
    # 전위 순회에서 왼쪽 서브트리
    left_pre = pre_order[1:root_idx + 1]
    # 재귀 함수
    post_order(left_pre, left_in)

    # 중위 순회에서 오른쪽 서브트리
    right_in = in_order[root_idx + 1:]
    # 전위 순회에서 오른쪽 서브트리
    right_pre = pre_order[root_idx + 1:]
    # 재귀 함수
    post_order(right_pre, right_in)

    # 루트 노드 출력
    print(pre_order[0], end='')


while True:
    try:
        pre_order, in_order = input().split()
        pre_order, in_order = list(pre_order), list(in_order)

        post_order(pre_order, in_order)
        print()
    except:
        break
