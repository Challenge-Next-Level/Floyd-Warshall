num_A, num_B = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

A_B = A.difference(B)
B_A = B.difference(A)

print(len(A_B.union(B_A)))