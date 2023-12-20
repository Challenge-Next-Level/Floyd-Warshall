N = int(input())
operator_list = list(input())

stack = list()

alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num_dict = dict()
for i in range(N):
    num_dict[alpha_list[i]] = input()

for o in operator_list:
    if o.isalpha():
        stack.append(num_dict[o])
    else:
        a = stack.pop()
        b = stack.pop()
        c = str(eval(b + o + a))
        stack.append(c)

print(format(float(stack[0]), ".2f"))
