# 어렵다
# https://chanu-ps.tistory.com/24

text = input()

left_k = list()
right_k = list()

cnt = 0
for s in text:
    if s == 'K':
        cnt += 1
    else:
        left_k.append(cnt)

cnt = 0
for s in text[::-1]:
    if s == 'K':
        cnt += 1
    else:
        right_k.append(cnt)

right_k.reverse()

start = 0
end = len(left_k) - 1
answer = 0

while start <= end:
    # end - start + 1 : 중간에 있는 R 의 개수 -> 중간에 K는 없다고 생각하는 건가?
    # 2 * min(left_k[start], right_k[end])) : 양 끝 K 위치
    answer = max(answer, end - start + 1 + 2 * min(left_k[start], right_k[end]))

    if left_k[start] < right_k[end]:
        start += 1
    else:
        end -= 1

print(answer)