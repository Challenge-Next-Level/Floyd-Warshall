"""
1~10까지 결과 리스트 생성 후, 답 찾는 방식
- 결과 리스트 생성 방식 :
    - 4 = 1+3, 2+2, 3+1 = 1+2+4 = 7
    - 5 = 2+3, 3+2, 4+1 = 2+4+7 = 13
"""

T = int(input())

result = [0, 1, 2, 4]

for i in range(4, 11):
    ans = result[i-1] + result[i-2] + result[i-3]
    result.append(ans)

for _ in range(T):
    n = int(input())
    print(result[n])
