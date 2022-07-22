# 13164(행복 유치원)을 풀고 풀어서 답이 쉽게 보였다. 원래는 아이디어가 필요한 어려운 문제임.
n = int(input())
k = int(input())
sensor = list(map(int, input().split()))

sensor.sort()
diff = []
for i in range(n-1):
    diff.append(sensor[i+1] - sensor[i])
# (n-1) - (k-1) = n-k
diff.sort()
print(sum(diff[:n-k]))