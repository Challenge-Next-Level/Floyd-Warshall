num = int(input())


def check(number): # 숫자에 홀수가 몇개인지 체크
    cnt = 0
    while number >= 10:
        n = number % 10
        if n % 2 != 0:
            cnt += 1
        number //= 10
    if number % 2 != 0:
        cnt += 1
    return cnt


reset = check(num)
minAns, maxAns = float('inf'), 0


def holic(number, count):
    cnt = check(number)
    if number // 10 == 0: # 한자리수일 때 리턴
        global minAns, maxAns
        minAns = min(minAns, count + cnt)
        maxAns = max(maxAns, count + cnt)
        return
    elif 0 < number // 10 < 9: # 두 자리수일 때
        first, second = number // 10, number % 10
        holic(first + second, count + cnt)
    else: # 세 자리수 이상일 때
        length = len(str(number))
        for i in range(1, length-1):
            for j in range(i+1, length):
                first, second, third = number%(10**i), (number%(10**j))//(10**i), number//(10**j)
                holic(first + second + third, count + cnt)


holic(num, 0)
print(minAns, maxAns)