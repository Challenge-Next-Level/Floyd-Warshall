# 인구수의 절반을 넘었을때의 위치에 우체국을 설치한다.

n = int(input()) #마을의 개수 n

array = [] #빈 리스트 생성
for i in range(n):
    x,y = map(int, input().split())
    array.append([x,y]) #마을의 위치, 인구수 [(x,a)]

array = sorted(array, key = lambda i : i[0]) #마을 위치 순서대로 array를 배열

pop = 0
for i in range(n):
    k = array[i][1] #인구수를 차례차례 더해서 총 인구수를 구한다.
    pop = pop + k

mid = pop//2 #인구수의 중간값을 구하기 위해 2로 나눈 몫을 구한다

if (pop%2) != 0:
    mid = mid + 1 #2로 나누어지지 않았을때는 올림을 해준다

pop_count = 0
for q,w in array:
    pop_count = pop_count + w #pop_count에 인구수를 누적시킨다.
    if pop_count >= mid: #누적된 인구수가 중간값과 같거나 넘어가는 순간
        ans = q #그 순간의 위치를 ans로 저장
        break
print(ans) #우체국의 위치 ans를 출력해준다.