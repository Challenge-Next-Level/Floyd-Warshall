"""
LCS : 최장 공통 부분 수열
- 공통 부분 수열의 첫 글자를 첫번째 문자열의 모든 위치에서 확인
- 결과를 담을 리스트 생성
    - 두번째 문자열 끝까지 갔을 시, 결과 리스트에 현재 결과를 담음
"""

fst = input()
scd = input()

ans = list()


# 현재 첫번재 문자의 위치와 두번째 문자의 위치, 이전 문자까지의 순열 길이
def solution(i, j, current):
    for k in range(i, len(fst)):
        for l in range(j, len(scd)):
            if fst[k] == scd[l]:
                next = current + 1

                if k == len(fst) - 1 or l == len(scd) - 1:
                    ans.append(next)
                    return

                solution(k + 1, l + 1, next)


for i in range(len(fst)):
    solution(i, 0, 0)

print(max(ans))
