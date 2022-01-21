N = int(input())
lope = []
for i in range(N):
    lope.append(int(input()))
lope.sort(reverse=True) # 튼튼한 로프부터 쓰기 위해 정렬
weight = lope[0] # 버틸 수 있는 무게
count = 1 # 사용한 로프 수
for i in range(1, N): # (사용한 로프 중 가장 약한것 * 로프수) 가 버틸 수 있는 무게
    count += 1
    weight = max(weight, lope[i] * count)
print(weight)