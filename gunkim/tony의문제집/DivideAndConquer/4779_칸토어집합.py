# EOF 처리를 무한 반복문 내에서 try, except으로 구현
while True:
    try:
        n = int(input())
        size = 3**n
        arr = ['-'] * size

        def divideAndConquer(start, length):
            if length == 1:
                return
            divide = length//3
            for i in range(start+divide*1, start+divide*2): # 중간지역 공백처리
                arr[i] = ' '
            divideAndConquer(start, divide)
            divideAndConquer(start+divide*2, divide)
            return

        divideAndConquer(0,size)
        print(''.join(arr))
    except:
        break