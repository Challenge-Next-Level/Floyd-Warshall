N, T = map(int, input().split())

bus_time = set()
for _ in range(N):
    S, I, C = map(int, input().split())

    for c in range(C):
        departure = S + I * c
        if departure >= T:
            if departure - T >= 2 ** 31:
                break

            bus_time.add(departure - T)

start = 0
if bus_time:
    end = max(bus_time)
else:
    print(-1)
    exit()

start_bus = min(bus_time)

answer = -1

while start <= end:
    mid = (start + end) // 2

    if mid >= start_bus:
        end = mid - 1
    else:
        start = mid + 1

    if mid in bus_time:
        answer = mid

print(answer)

