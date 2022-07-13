import sys

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().split()[0])
    order = []
    for _ in range(2):
        order.append(list(map(int, sys.stdin.readline().split())))

    preorder = order[0] # 전위순회 순서
    inorder = order[1] # 중위순회 순서
    answer = []
    visit = [0 for _ in range(n+1)] # preorder의 인덱스를 기준으로 방문체크


    def postSearch(root, start, end): # preorder에서 root idx를 통한 root node 참고, inorder에서 tree의 start/end 구간
        if visit[root] == 1: # 방문한 노드면 리턴(백트래킹)
            return
        visit[root] = 1

        x = -1
        for i in range(start, end+1): # preorder root idx를 통해 inorder에서 실제 root의 위치 찾기
            if preorder[root] == inorder[i]:
                x = i
        leftSize = x - start # 왼쪽 서브트리 사이즈
        rightSize = end - x # 오른쪽 서브트리 사이즈

        if leftSize > 0: # 왼쪽 서브트리 탐색
            postSearch(root+1, start, x-1)
        if rightSize > 0: # 오른쪽 서브트리 탐색
            postSearch(root+leftSize+1, x+1, end)
        answer.append(preorder[root])
        return


    postSearch(0, 0, n-1)
    print(' '.join(list(map(str, answer))))