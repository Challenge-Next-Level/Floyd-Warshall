import sys

input = sys.stdin.readline

S = input().rstrip()
P = input().rstrip()


# KMP 테이블 : 동일 접두사-접미사 테이블
# KMP[i] = 패텅 P에서 i번째 문자열까지 고려했을 때, 접두사-접미사가 일치하는 최대 길이 값
def KMP_table(pattern):
    pattern_length = len(pattern)
    table = [0 for _ in range(pattern_length)]

    # 패턴의 인덱스 접근(접두사)
    header_idx = 0
    # 패턴의 인덱스 접근(접미사)
    for tail_idx in range(1, pattern_length):
        # header_idx가 0이 되거나, header_idx와 tail_idx번째 글자가 같아질때까지 진행
        while header_idx > 0 and pattern[header_idx] != pattern[tail_idx]:
            #
            header_idx = table[header_idx - 1]

        # 값이 일치하는 경우, header_idx 1 증가시키고 그 값을 table에 저장
        if pattern[header_idx] == pattern[tail_idx]:
            header_idx += 1
            table[tail_idx] = header_idx

    return table


kmp_table = KMP_table(P)

answer = 0
pattern_idx = 0

for idx in range(len(S)):
    # 단어와 패턴이 일치하지 않는 경우, pattern_idx를 table을 활용해 값 변경
    while pattern_idx > 0 and S[idx] != P[pattern_idx]:
        pattern_idx = kmp_table[pattern_idx - 1]

    # 해당 인덱스에서 값이 일치한다면, pattern_idx를 1 증가시킴
    # 만약 pattern_idx가 패턴의 끝까지 도달한다면, 시작 인덱스 값을 계산하여 추가 후 pattern_idx 값 table의 인덱스에 접근하여 변경
    if S[idx] == P[pattern_idx]:
        if pattern_idx == len(P) - 1:
            answer = 1
            break
        else:
            pattern_idx += 1

print(answer)
