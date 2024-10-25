import sys

input = sys.stdin.readline

N = int(input())
switch_list = [0] + list(map(int, input().split()))

S = int(input())
for _ in range(S):
    sex, idx = map(int, input().split())

    if sex == 1:
        for i in range(idx, N + 1, idx):
            switch_list[i] = abs(switch_list[i] - 1)
    else:
        for i in range(min(idx, N - idx + 1)):
            if i == 0:
                switch_list[idx] = abs(switch_list[idx] - 1)
            else:
                if switch_list[idx - i] == switch_list[idx + i]:
                    switch_list[idx - i] = abs(switch_list[idx - i] - 1)
                    switch_list[idx + i] = abs(switch_list[idx + i] - 1)
                else:
                    break

for i in range(1, N + 1, 20):
    print(*switch_list[i:min(i + 20, N + 1)])
