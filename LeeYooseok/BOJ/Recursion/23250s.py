# n이 짝수일때 : 1->2 를 먼저 시행
# n이 홀수일때 : 1->3 를 먼저 시행

n, k = map(int, input().split())

if n % 2 == 0:
    print("t")
else:
    print("s")
