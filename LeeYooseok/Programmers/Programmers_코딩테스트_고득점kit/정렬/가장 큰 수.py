def solution(numbers):
    # 3번씩 이어 붙인 문자열들을 내림차순으로 정렬
    numbers = sorted(numbers, key=lambda x: str(x) * 3, reverse=True)

    # 문자열들을 전부 이어 붙인다.
    answer = ''.join(map(str, numbers))

    # numbers의 원소가 모두 0일 때
    return answer if int(answer) != 0 else '0'