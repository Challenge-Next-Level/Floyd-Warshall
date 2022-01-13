a, b = input().split()
len_diff = len(b) - len(a)
min_diff = float('inf') # 차이의 최솟값을 저장할 곳
for i in range(len_diff + 1): # b문자열에서 a문자열 길이만큼의 구만마다 문자열을 잘라 비교를 한다
    slice_b = b[i:i + len(a)]
    count = 0
    for j in range(len(a)):
        if a[j] != slice_b[j]:
            count += 1
    min_diff = min(min_diff, count)
print(min_diff)