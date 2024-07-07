from string import ascii_uppercase
alpha_list = list(ascii_uppercase)

alpha_dic = {}
for i in alpha_list:
    alpha_dic[i] = 0

S = input().upper()

for m in S:
    alpha_dic[m] += 1

result_list = list(alpha_dic.values())
result_num = max(result_list)
result_list.remove(result_num)
result = result_num in result_list
if result == True:
    print("?")
else:
    for k,v in alpha_dic.items():
        if result_num == v:
            print(k)