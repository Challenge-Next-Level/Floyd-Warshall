# 가장 큰 감소하는 수 : 9876543210

decreasing_num_set = list()

def make_decreasing_num(now_num):
    for i in range(10):
        if i > int(now_num[0]):
            new_num = str(i) + now_num
            decreasing_num_set.append(int(new_num))

            make_decreasing_num(new_num)

for j in range(10):
    make_decreasing_num(str(j))
    decreasing_num_set.append(j)

decreasing_num_set.sort()

try:
    print(decreasing_num_set[int(input())])
except:
    print(-1)
