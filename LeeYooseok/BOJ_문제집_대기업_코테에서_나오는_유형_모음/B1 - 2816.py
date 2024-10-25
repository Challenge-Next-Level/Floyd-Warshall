N = int(input())

kbs1_idx, kbs2_idx = 0, 0

for i in range(N):
    channel = input()
    if channel == "KBS1":
        kbs1_idx = i
    if channel == "KBS2":
        kbs2_idx = i

answer = ""

answer += "1" * kbs1_idx  # KBS1이 있는 곳으로 1번을 이용해서 화살표를 내린다.
answer += "4" * kbs1_idx  # KBS1을 4번을 이용해서 첫번째로 올린다. 이후, 화살표는 첫 번째 인덱스를 가리킨다.

if kbs1_idx > kbs2_idx:  # 처음에 KBS1이 KBS2보다 아래에 있을 경우, KBS1을 첫번째로 보내는 과정에서 KBS2가 한칸 아래로 내려간다.
    kbs2_idx += 1

answer += "1" * kbs2_idx  # KBS2가 있는 곳으로 1번을 이용해서 화살표를 내린다.
answer += "4" * (kbs2_idx - 1)  # KBS2을 4번을 이용해서 두번째로 올린다.

print(answer)
