import sys

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().split()[0])
    order = []
    for _ in range(2):
        order.append(list(map(int, sys.stdin.readline().split())))

    preorder = order[0]
    inorder = order[1]
    answer = []
    visit = [0 for _ in range(n+1)]
    idx = 0

    def postSearch(rootIdx, size):
        if not 0 <= rootIdx < n:
            return
        if visit[rootIdx] == 1:
            return
        visit[rootIdx] = 1
        node = preorder[rootIdx]
        newRootIdx = -1
        for i in range(size):
            if inorder[rootIdx+i] == node:
                newRootIdx = rootIdx+i
                break
        print(visit)
        leftSize = newRootIdx-rootIdx
        rightSize = size - leftSize - 1
        if visit[newRootIdx+1] == 0:
            postSearch(rootIdx+1, leftSize)
        if newRootIdx != -1:
            if node == 5:
                print('hi2')
            postSearch(rootIdx+leftSize, rightSize)
        print("node", node)
        return


    postSearch(0, n)
    print(answer)