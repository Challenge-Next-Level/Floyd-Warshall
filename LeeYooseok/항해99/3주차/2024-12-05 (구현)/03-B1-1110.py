N = input()


def operator(number):
    num = int(number)
    if num >= 10:
        num = int(number[0]) + int(number[1])

    return number[-1] + str(num)[-1]


answer = 1
now_number = operator(N)
while int(now_number) != int(N):
    now_number = operator(now_number)
    answer += 1

print(answer)
