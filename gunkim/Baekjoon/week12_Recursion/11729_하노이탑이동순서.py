def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    # target, start, end 는 중 각각 하나는 첫 번째, 두 번째, 세 번째 막대기를 의미한다.
    # 따라서 셋의 합은 항상 6이 되는 것이다, 두 개의 막대기를 파악하면 나머지 막대기가 몇 번째 인지 알 수 있다
    target = 6 - start - end
    hanoi(n - 1, start, target) # n - 1개의 쌓여있던 원판들을 한 곳으로 모두 이동시키는 작업
    print(start, end) # 맨 아래 원판을 목표 지점에 이동시키는 작업
    hanoi(n - 1, target, end) # n - 1개의 원판들도 이제 목표 지점에 이동시키는 작업


N = int(input())
print((2 ** N) - 1) # 횟수는 공식과 같이 구할 수 있다
hanoi(N, 1, 3)