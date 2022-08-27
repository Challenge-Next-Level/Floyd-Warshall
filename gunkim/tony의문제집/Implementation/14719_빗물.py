h, w = map(int, input().split())
block = list(map(int, input().split()))


space = []
idx = 0
while idx < w-1:
    if block[idx] > block[idx + 1]: # 내려가는 구간이 생길 때 고이는 구간을 탐색
        maxH = [-1, -1]
        for j in range(idx+1, w):
            if maxH[0] < block[j]:
                maxH = [block[j], j]
            if block[j] >= block[idx]:
                space.append([idx,j])
                idx = j
                break
        if maxH[0] < block[idx]:
            space.append([idx, maxH[1]])
            idx = maxH[1]
    else:
        idx += 1

answer = 0
for i in range(len(space)):
    start, end = space[i]
    minH = min(block[start], block[end])
    for j in range(start+1, end):
        answer += minH-block[j]
print(answer)