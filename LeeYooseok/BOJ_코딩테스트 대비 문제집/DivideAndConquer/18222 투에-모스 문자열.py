# k = int(input())
#
#
# def solve(X_list, n):
#     if n >= k:
#         print(X_list[k - 1])
#         return
#
#     reverse_X_list = X_list[:]
#     for x in range(n):
#         if reverse_X_list[x] == 0:
#             reverse_X_list[x] = 1
#         else:
#             reverse_X_list[x] = 0
#
#     X_list.extend(reverse_X_list)
#
#     solve(X_list, n * 2)
#
#
# solve([0], 1)

k = int(input())
def recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n%2:
        return 1-recursive(n//2)
    else:
        return recursive(n//2)
print(recursive(k-1))