a, b = map(int, input().split())
if b > 10000000:
    b = 10000000
prime = [True for _ in range(b+1)]
prime[0], prime[1] = False, False

for num in range(2, b+1):
    if prime[num] is False:
        continue
    idx = 2
    while num * idx <= b:
        if prime[num * idx] is False:
            idx += 1
            continue
        prime[num * idx] = False
        idx += 1

for num in range(a, b+1):
    if prime[num]:
        number = str(num)
        length = len(number)
        if length == 1:
            print(number)
        else:
            centerIdx = length // 2
            flag = 0
            for i in range(centerIdx):
                if number[i] != number[length-1-i]:
                    flag = 1
                    break
            if flag == 0:
                print(number)
print(-1)