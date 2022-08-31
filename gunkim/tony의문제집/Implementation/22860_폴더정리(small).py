# 재귀 깊이 설정 필요
# 폴더이름은 중복이 없을 거다 라는 가정이 맞았음. 폴더 이름을 통해 하위 폴더/파일 들을 find(재귀)로 찾음
# 문자열을 여러 구분자를 기준으로 두어 split하려고 했는데 이때 re 라는 모듈을 사용
import sys, re
sys.setrecursionlimit(10**8)

n, m = map(int, sys.stdin.readline().split())
folder = {}
for _ in range(n+m):
    parent, node, isFolder = sys.stdin.readline().split()
    if isFolder == '1' and node not in folder:
        folder[node] = []
    if parent not in folder:
        folder[parent] = [node]
    else:
        folder[parent].append(node)


def find(fold):
    global result
    for f in folder[fold]:
        if f not in folder:
            result.append(f)
        else:
            find(f)


q = int(input())
result = []
for _ in range(q):
    folders = list(re.split('[/\n]', sys.stdin.readline()))
    find(folders[-2])
    print(len(set(result)), len(result))
    result = []