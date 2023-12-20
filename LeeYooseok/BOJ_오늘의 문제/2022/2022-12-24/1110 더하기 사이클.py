N = int(input())
temp_num = str(N)
answer = 0

def cycle():
    global temp_num
    if len(temp_num) < 2:
        temp_num = '0' + temp_num

    add_num = int(temp_num[0]) + int(temp_num[-1])
    temp_num = temp_num[-1] + str(add_num)[-1]

cycle()
answer += 1


while int(temp_num) != N:
    cycle()
    answer += 1

print(answer)