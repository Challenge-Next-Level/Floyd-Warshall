# 정렬 방법 - 선택 정렬

def solution(p):
    n = len(p)
    result = [0] * n # 각 위치의 값이 변경된 횟수

    # 최종 목표 - 오름차순 정렬
    sorted_p = sorted(p)

    # p가 오름차순으로 정렬될 때까지 무한 반복
    while sorted_p != p:
        # 1) 배열 인덱스를 나타내는 정수 idx 를 0 으로 초기화 합니다.
        idx = 0
        # 4-1) idx 가 n 보다 작다면 2번 단계로 돌아갑니다.
        while idx < n:
            # 2) 가장 작은 수를 찾음 - 가장 작은 수의 인덱스는 idx_p_j 입니다.
            p_j = min(p[idx:])
            idx_p_j = p.index(p_j)

            # 3) idx 와 idx_p_j 가 다르면 p[idx] 와 p[idx_p_j] 의 값을 서로 바꿉니다.
            if idx != idx_p_j:
                p[idx], p[idx_p_j] = p[idx_p_j], p[idx]
                result[idx] += 1
                result[idx_p_j] += 1
            # 4) idx 에 1을 더합니다.
            idx += 1
    return result


print(solution([2, 5, 3, 1, 4]))
