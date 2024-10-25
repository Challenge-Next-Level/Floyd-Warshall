N = int(input())
M = int(input())
light_loc_list = list(map(int, input().split()))

left, right = 0, N
answer = N


def check(height):
    if height < light_loc_list[0]:
        return False

    for i in range(M - 1):
        if (light_loc_list[i + 1] - light_loc_list[i]) > 2 * height:
            return False

    if height < (N - light_loc_list[-1]):
        return False

    return True


while left <= right:
    mid = (left + right) // 2

    if check(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
