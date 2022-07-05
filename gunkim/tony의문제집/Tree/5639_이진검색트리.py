# 오른쪽 서브 트리를 찾아낼 수 있음을 활용
# 이때 왼쪽, 오른쪽 서브 트리를 재귀로 계속 찾아간다
# 노드의 출력을 이때 왼쪽서브트리, 오른쪽서브트리, 해당노드 순으로 하면 후위탐색 출력 순이 된다.
import sys

sys.setrecursionlimit(10 ** 9) # RecursionError가 발생하여 한도를 강제로 설정하여 높인다.

tree = []
count = 0
while count <= 10000:
    try: # 입력 값이 몇 개 들어오는지 모르기 때문에 try, except을 활용
        temp = int(input())
    except:
        break
    tree.append(temp)
    count += 1


def solution(start, end):
    if start > end: # 탐색 종료 조건
        return

    div = end + 1

    for i in range(start + 1, end + 1):
        # 루트 보다 큰 지점 --> 오른쪽 서브 트리 시작점
        if tree[start] < tree[i]:
            div = i
            break

    solution(start + 1, div - 1) # 왼쪽 서브 트리 탐색
    solution(div, end) # 오른쪽 서브 트리 탐색
    print(tree[start]) # 해당 노드 출력


treeLength = len(tree) - 1
solution(0, treeLength)
