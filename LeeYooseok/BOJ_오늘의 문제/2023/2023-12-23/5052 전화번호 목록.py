t = int(input())

for _ in range(t):
    n = int(input())

    phone_number = [input() for _ in range(n)]

    # 한 번호가 다른 번호의 접두어라면, 배열을 정렬했을 때 그 두 번호는 인접해 있습니다.
    # arr = ["2346", "123", "123455", "234", "2345", "123456"]

    # arr.sort()
    # ['123', '123455', '123456', '234', '2345', '2346']

    phone_number.sort()

    answer = True
    for i in range(len(phone_number) - 1):
        # 겹치는게 있다면, False
        if phone_number[i] == phone_number[i + 1][:len(phone_number[i])]:
            answer = False
            break

    if answer:
        print("YES")
    else:
        print("NO")
