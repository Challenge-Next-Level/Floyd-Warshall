T = int(input())
for _ in range(T):
    answer = ""
    c, p = map(int, input().split())

    # 정수부
    answer += str(c // p)
    answer += "."

    # c = c 를 p로 나눈 나머지
    c = (c % p)

    # 소수부
    # 순환부 start, end
    start, end = len(answer), len(answer)
    # 나머지 list
    # mod_list[i] = 나머지 i 가 발생했던 answer 의 위치
    mod_list = [-1 for _ in range(100000)]
    while True:
        mod = c % p * 10
        c = mod
        if mod_list[mod] != -1:
            start = mod_list[mod]
            break
        end += 1
        mod_list[mod] = end
        answer += str(c // p)

    print(answer[:start-1] + "(" + answer[start-1:] + ")")