# 시간초과로 개고생 했는데 nodeIdx를 만들어 놓고 search안에서 x 값을 구하는 반복문을 없앨 수 있었음
import sys
sys.setrecursionlimit(10**9)
n = int(sys.stdin.readline().split()[0])
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
visit = [0 for _ in range(n)]
nodeIdx = {}
for i in range(n):
    nodeIdx[inorder[i]] = i
answer = []


# 전위순회: root -> left -> right
def search(root, start, end):
    if visit[root] == 1:
        return
    visit[root] = 1

    x = nodeIdx[postorder[root]]

    leftSize = x - start
    rightSize = end - x

    answer.append(postorder[root])
    if leftSize > 0:
        search(root-rightSize-1, start, x-1)
    if rightSize > 0:
        search(root-1, x+1, end)
    return


search(n-1, 0, n-1)
print(' '.join(list(map(str, answer))))