# 리프 노드 : 차수(연결된 노드)가 1인 노드
# root -> 리프의 부모 노드까지 1자형 트리 -> 리프 m(root 노드 포함)개 만족
# root -> 리프의 부모 노드 개수 : (n - (m + 1))

n, m = map(int, input().split())

for i in range(n - m):
    print(i, i + 1)

for j in range(n - m + 1, n):
    print(n - m, j)
