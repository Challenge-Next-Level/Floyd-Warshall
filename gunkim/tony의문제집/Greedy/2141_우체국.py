# 정말 단순한 생각인데 'Greedy'라는 이름에 속아 해결법을 생각해내지 못함.
# 해결 논리는 초딩도 생각할 수 있는 풀이
import sys

n = int(input())
population = [] # 지점별 인구수 저장
total = 0 # 전체 인구 수
for _ in range(n):
    x, a = map(int, sys.stdin.readline().split())
    population.append([x, a])
    total += a
population.sort() # 지점 순서로 정렬 필수(틀린 이유)

isHalf = 0
halfPopulation = total / 2
flag = 0
for i in range(n):
    isHalf += population[i][1]
    if isHalf >= halfPopulation: # 절반 인구 수를 넘었을 때
        print(population[i][0]) # 우체국을 효율적으로 짓게되는 곳
        flag = 1
    if flag == 1:
        break