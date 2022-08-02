n = int(input())
k = int(input())
pointList = list(map(int, input().split()))
pointList.sort()

if k >= n:
    print(0)
    exit()

distanceList = list()
for idx in range(1, n):
    distanceList.append(pointList[idx] - pointList[idx-1])

distanceList.sort(reverse=True)
for _ in range(k-1):
    distanceList.pop()

print(sum(distanceList))
