# 직접 moo를 찾게 되면 당연히! 시간초과가 발생한다.
n = int(input())
mooSize = 3
k = 0
while mooSize < n: # n번 째 숫자를 찾을 수 있는 최소글자수의 moo를 찾는다
    k += 1
    mooSize = mooSize*2 + (k+3)


def divideAndConquer(size, midSize, idx): # 앞, 중간, 뒤 영역으로 나누어 n번째 숫자를 찾는다
    front = (size-midSize) // 2
    if idx <= front: # 앞 부분에 있다면
        return divideAndConquer(front, midSize-1, idx)
    elif idx > front + midSize: # 뒷 부분에 있다면
        return divideAndConquer(front, midSize-1, idx-front-midSize)
    else: # 중간에 있다면
        if idx - front == 1: # 첫 번째 글자만 m이다, 나머진 o
            return 'm'
        else:
            return 'o'


print(divideAndConquer(mooSize, k+3, n))