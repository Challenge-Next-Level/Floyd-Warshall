"""
V, L, D = 한번만 사용
I, X, C, M = 연속해서 3번까지 사용 가능
"""
roma_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roma_nums2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}  # 1번만 사용 가능

nums = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
        4: 'IV', 1: 'I'}

str1 = input()
str2 = input()


def str_to_num(string):
    num = 0

    for roma_num in roma_nums2.keys():
        if roma_num in string:
            num += roma_nums2[roma_num]
            string = string.replace(roma_num, '')

    for s in string:
        num += roma_nums[s]

    return num


num1 = str_to_num(str1)
num2 = str_to_num(str2)

num_result = num1 + num2

print(num_result)

one_str = ['V', 'L', 'D', 'IV', 'IX', 'XL', 'XC', 'CD', 'CM']
other_str = {'I': 0, 'X': 0, 'C': 0, 'M': 0}


def num_to_str(num):
    result = ''
    i = 0

    while num != 0:
        current_nums = list(nums.keys())
        current_num = current_nums[i]

        if current_num in list(other_str.keys()):
            if other_str.get(current_num) == 3:
                if current_nums[i-1] < num:
                    i -= 1
                else:
                    i += 1
                other_str[current_num] = 0
                continue
            else:
                other_str[current_num] += 1

        if num >= current_num:
            num = num - current_num
            current_str = nums.get(current_num)
            result += current_str
            if current_str in one_str:
                i += 1

        else:
            i += 1

    return result

print(num_to_str(num_result))